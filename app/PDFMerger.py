from datetime import datetime
from pathlib import Path

import PyPDF2

import exceptions


class Merger:
    def __init__(self, args):
        path = Path(args.path)
        self.pdfWriter = PyPDF2.PdfFileWriter()
        self.path: Path = path
        self.pdf_files: list[str] = args.files
        self.output_path: Path = Path(args.output) or path

    def merge_files(self):
        self._validate()

        for file in self._get_files():
            pdf_file = file.open(mode='rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)

            for nr in range(0, pdf_reader.numPages):
                page = pdf_reader.getPage(nr)
                self.pdfWriter.addPage(page)

        self._write_merged_files()

    def _get_files(self) -> list[Path]:
        if self.pdf_files:
            return [self.path.joinpath(file if file.endswith(".pdf") else f"{file}.pdf") for file in self.pdf_files]

        pdf_files = [filename for filename in self.path.iterdir() if filename.suffix == ".pdf"]
        pdf_files.sort(key=lambda item: item.name.lower())

        if not pdf_files:
            raise exceptions.FilesNotFoundInDirectoryError(self.path.name)

        return pdf_files

    def _write_merged_files(self):
        filename = datetime.now().strftime('%Y-%m-%d_%H%M%S_merged')
        pdf_output = open(self.output_path.joinpath(f"{filename}.pdf"), 'wb')
        self.pdfWriter.write(pdf_output)
        pdf_output.close()

    def _validate(self):
        if not self.path.exists():
            raise exceptions.PathNotExistsError(self.path)
        if not self.output_path.exists():
            self.output_path.mkdir()
