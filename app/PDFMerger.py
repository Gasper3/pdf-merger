from datetime import datetime

import PyPDF2
import os


class Merger:
    def __init__(self, args):
        self.pdfWriter = PyPDF2.PdfFileWriter()
        self.path: str = args.path
        self.pdf_files: list[str] = args.files
        self.output_path: str = args.output or self.path

    def merge_files(self):
        self._validate_args()

        try:
            for filename in self._get_files():
                pdf_file = open(self.path + filename, 'rb')
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)

                for nr in range(0, pdf_reader.numPages):
                    page = pdf_reader.getPage(nr)
                    self.pdfWriter.addPage(page)

            self._write_merged_files()
        except FileNotFoundError as e:
            print(e)
            exit(1)

    def _get_files(self) -> list[str]:
        pdf_files = self.pdf_files or [filename for filename in os.listdir(self.path) if filename.endswith('.pdf')]
        pdf_files.sort(key=str.lower)

        if not pdf_files:
            raise FileNotFoundError(f"There are no pdf files in {self.path}")

        for index, filename in enumerate(pdf_files):
            if not filename.endswith(".pdf"):
                pdf_files[index] += ".pdf"

        return pdf_files

    def _write_merged_files(self):
        filename = datetime.now().strftime('%Y-%m-%d_%H%M%S')
        pdf_output = open(self.output_path + f'{filename}.pdf', 'wb')
        self.pdfWriter.write(pdf_output)
        pdf_output.close()


    def _validate_args(self):
        if not self.path.endswith("/"):
            self.path += "/"

        if not self.output_path.endswith("/"):
            self.output_path += "/"

        for path in [self.path, self.output_path]:
            if not os.path.exists(path):
                print(f"Path: {path} not found")
                exit(1)