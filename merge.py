import PyPDF2
import os
import sys
from datetime import datetime

arguments = sys.argv[1:]
if not arguments:
    print('There is no path passed to program')
    exit(1)

path = arguments[0]
if not path.endswith('/'):
    path += '/'

pdfFiles = [filename for filename in os.listdir(path) if filename.endswith('.pdf')]

if not pdfFiles:
    print(f'There are 0 pdf files in: {path}')
    exit(1)

pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    pdfFileObj = open(path + filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

filename = datetime.now().strftime('%Y-%m-%d_%H%M%S')
pdfOutput = open(path + f'{filename}.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
