from datetime import datetime

import PyPDF2
import os
import sys


arguments = sys.argv[1:]
if not arguments:
    print('There is no path passed to program')
    exit(1)

path = arguments[0]
if not path.endswith('/'):
    path += '/'

pdfFilesArg = sys.argv[2:]
pdfFiles = pdfFilesArg or [filename for filename in os.listdir(path) if filename.endswith('.pdf')]
pdfFiles.sort(key=str.lower)

if not pdfFiles:
    print(f'There are no pdf files in: {path}')
    exit(1)

pdfWriter = PyPDF2.PdfFileWriter()

try:
    for filename in pdfFiles:
        pdfFileObj = open(path + filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        for pageNum in range(0, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
except FileNotFoundError:
    print(f'There are no file {filename} in {path}')
    exit(1)

filename = datetime.now().strftime('%Y-%m-%d_%H%M%S')
pdfOutput = open(path + f'{filename}.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
