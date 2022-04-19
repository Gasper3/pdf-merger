from pathlib import Path

import pytest


@pytest.fixture()
def resources_path() -> Path:
    return Path("tests/resources")
