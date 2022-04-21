from pathlib import Path


class FilesNotFoundInDirectoryError(Exception):
    def __init__(self, directory):
        self.message = f"Files not found in given directory: {directory}"
        super().__init__(self.message)


class PathNotExistsError(Exception):
    def __init__(self, path: Path):
        self.message = f"Path not exists: {path.resolve()}"
        super().__init__(self.message)
