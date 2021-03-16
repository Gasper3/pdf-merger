import sys
from PDFMerger import Merger

arguments = sys.argv[1:]
if not arguments:
    print('There is no path passed to program')
    exit(1)

path = arguments[0]
if not path.endswith('/'):
    path += '/'

pdfFilesArg = sys.argv[2:]

Merger(path, pdfFilesArg).merge_files()
