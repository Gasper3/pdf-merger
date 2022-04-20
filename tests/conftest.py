from pathlib import Path

import pytest

from .helpers import remove_created_files


@pytest.fixture()
def resources_path() -> Path:
    path = Path("tests/resources")
    yield path

    remove_created_files(path)
