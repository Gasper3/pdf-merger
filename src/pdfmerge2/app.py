import argparse
import logging
import os
from pathlib import Path

from .exceptions import FilesNotFoundInDirectoryError, PathNotExistsError
from .merger import Merger

is_debug = os.getenv("MERGER_DEBUG")
# logger = logging.Logger(__name__, level=logging.DEBUG if is_debug else logging.ERROR)
# log_formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
# file_handler = logging.FileHandler(Path("log/app.log"), mode='a' if not is_debug else 'w')
# file_handler.setFormatter(log_formatter)
# logger.addHandler(file_handler)


def run():
    parser = argparse.ArgumentParser(description="Merge .pdf files")
    parser.add_argument("-o", "--output", help="Path where merged file will be saved", type=str)
    parser.add_argument("-f", "--files", help="Merge only these files", type=str, metavar="name", nargs="+")
    parser.add_argument('path', help="Path to pdf files", type=str)

    args = parser.parse_args()

    merger = Merger(args.path, args.files, args.output)

    try:
        merger.merge_files()
    except PathNotExistsError as e:
        # logger.error(e)
        print("Provided path does not exist" if not is_debug else e)
    except FilesNotFoundInDirectoryError as e:
        # logger.error(e)
        print("Files not found" if not is_debug else e)
    except FileNotFoundError as e:
        # logger.error(e)
        print("File not found" if not is_debug else e)
    except Exception as e:
        # logger.error(e)
        print("Error occured" if not is_debug else e)
    else:
        print(f"Files merged into: {merger.merged_file_name}")
