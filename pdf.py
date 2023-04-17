import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PyPDF2 import PdfFileMerger


class PDFHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.pdf'):
            time.sleep(1)  # wait for the file to finish copying
            pdf_dir = os.path.dirname(event.src_path)
            pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
            merger = PdfFileMerger()
            for pdf in pdf_files:
                pdf_path = os.path.join(pdf_dir, pdf)
                merger.append(pdf_path)
            merged_path = os.path.join(pdf_dir, 'merged.pdf')
            merger.write(merged_path)
            merger.close()
            logging.info(f'Merged PDF files in {pdf_dir} to {merged_path}')


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    pdf_dir = '~/Downloads'
    event_handler = PDFHandler()
    observer = Observer()
    observer.schedule(event_handler, pdf_dir, recursive=False)
    observer.start()
    logging.info(f'Watching {pdf_dir} for new PDF files...')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
