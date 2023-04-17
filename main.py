import os
from PyPDF2 import PdfMerger, PdfReader


downloads_dir = os.path.expanduser('~/Downloads')
pdf_dir = os.path.expanduser('~/Downloads/PDF')


if not os.path.exists(pdf_dir):
    os.mkdir(pdf_dir)

pdf_files = [f for f in os.listdir(downloads_dir) if f.endswith('.pdf')]
merger = PdfMerger()
for pdf_file in pdf_files:

    with open(os.path.join(downloads_dir, pdf_file), 'rb') as f:
        pdf_reader = PdfReader(f)
        merger.append(pdf_reader)


merged_file_path = os.path.join(pdf_dir, 'merged_file.pdf')


with open(merged_file_path, 'wb') as f:
    merger.write(f)
