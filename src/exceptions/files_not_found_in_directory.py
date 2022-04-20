class FilesNotFoundInDirectoryError(Exception):
    def __init__(self, directory):
        self.message = f"Files not found in given directory: {directory}"
        super().__init__(self.message)
