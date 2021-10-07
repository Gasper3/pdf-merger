import sys
from app.PDFMerger import Merger

def main():
    arguments = sys.argv[1:]
    if not arguments:
        print('There is no path passed to program')
        exit(1)

    path = arguments[0]
    if not path.endswith('/'):
        path += '/'

    pdfFilesArg = sys.argv[2:]

    Merger(path, pdfFilesArg).merge_files()

if __name__ == "__main__":
    main()
