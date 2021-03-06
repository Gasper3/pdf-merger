from datetime import datetime

import PyPDF2
import os


class Merger:
    def __init__(self, path, pdf_files):
        self.pdfWriter = PyPDF2.PdfFileWriter()
        self.path = path
        self.pdf_files = pdf_files

    def _get_files(self):
        pdf_files = self.pdf_files or [filename for filename in os.listdir(self.path) if filename.endswith('.pdf')]
        pdf_files.sort(key=str.lower)

        if not pdf_files:
            print(f'There are no pdf files in: {self.path}')
            exit(1)

        return pdf_files

    def merge_files(self):
        try:
            for filename in self._get_files():
                pdf_file = open(self.path + filename, 'rb')
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                for nr in range(0, pdf_reader.numPages):
                    page = pdf_reader.getPage(nr)
                    self.pdfWriter.addPage(page)
        except FileNotFoundError:
            print(f'There are no file {filename} in {self.path}')
            exit(1)

        filename = datetime.now().strftime('%Y-%m-%d_%H%M%S')
        pdf_output = open(self.path + f'{filename}.pdf', 'wb')
        self.pdfWriter.write(pdf_output)
        pdf_output.close()
