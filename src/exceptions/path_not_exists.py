from pathlib import Path


class PathNotExistsError(Exception):
    def __init__(self, path: Path):
        self.message = f"Path not exists: {path.resolve()}"
        super().__init__(self.message)
