from src.pdfmerge2.merger import Merger
from .helpers import create_args, get_contents_names
from PyPDF2 import PdfFileReader


def test_merge_from_path(resources_path):
    args = create_args()
    merger = Merger(**args)

    merger.merge_files()

    assert merger.merged_file_path.name in get_contents_names(resources_path)
    with merger.merged_file_path.open(mode='rb') as merged_file:
        reader = PdfFileReader(merged_file)
        assert 12 == len(reader.pages)


def test_merge_to_output_not_exist(resources_path):
    output_path = resources_path.joinpath("new_output")
    args = create_args(output=output_path)
    merger = Merger(**args)

    merger.merge_files()

    assert merger.merged_file_path.name in get_contents_names(output_path)
    with merger.merged_file_path.open(mode='rb') as merged_file:
        reader = PdfFileReader(merged_file)
        assert 12 == len(reader.pages)


def test_merge_specified_files(resources_path):
    args = create_args(pdf_files=['pdf1', 'pdf2'])
    merger = Merger(**args)

    merger.merge_files()

    assert merger.merged_file_path.name in get_contents_names(resources_path)
    with merger.merged_file_path.open(mode='rb') as merged_file:
        reader = PdfFileReader(merged_file)
        assert 6 == reader.numPages

