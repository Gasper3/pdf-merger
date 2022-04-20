from app.PDFMerger import Merger
from .helpers import create_args, get_contents_names, check_merged_file, remove_created_files


def test_merge_from_path(resources_path):
    args = create_args()
    merger = Merger(**args)

    merger.merge_files()

    pdf_file = resources_path.joinpath(merger.merged_file_name).open(mode='rb')
    check_merged_file(pdf_file)

    assert merger.merged_file_name in get_contents_names(resources_path)


def test_merge_to_output_not_exist(resources_path):
    output_path = resources_path.joinpath("new_output")
    args = create_args(output=output_path)
    merger = Merger(**args)

    merger.merge_files()

    pdf_file = output_path.joinpath(merger.merged_file_name).open(mode='rb')
    check_merged_file(pdf_file)

    assert merger.merged_file_name in get_contents_names(output_path)
