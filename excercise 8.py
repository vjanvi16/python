
from pyPDF2 import pdfwriter
import os 
merger = pdfwriter()
files = [file or file in os.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()