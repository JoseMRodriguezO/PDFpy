import os
from PyPDF2 import PdfFileMerger, PdfFileReader

# Set the directory path where your PDF files are stored
pdf_dir = '/path/to/pdf/files/'

# Get a list of all the PDF files in the directory
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]

# Create a PdfFileMerger object
merger = PdfFileMerger()

# Loop through each PDF file and append it to the merger object
for pdf_file in pdf_files:
    # Open the PDF file in read-binary mode
    with open(os.path.join(pdf_dir, pdf_file), 'rb') as f:
        pdf_reader = PdfFileReader(f)
        merger.append(pdf_reader)

# Write the merged PDF file to a new file
with open(os.path.join(pdf_dir, 'merged.pdf'), 'wb') as f:
    merger.write(f)
