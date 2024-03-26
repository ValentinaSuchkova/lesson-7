import os
import pytest
import zipfile
import shutil
from settings_os import ARCHIVE_PATH, FILES_PATH, ARCHIVE


@pytest.fixture(scope='session', autouse=True)
def zip_to_archive():
    """Запаковывает в архив файлы и удаляет архив после тестов"""
    if not os.path.exists(ARCHIVE_PATH):
        os.mkdir(ARCHIVE_PATH)
    with zipfile.ZipFile(ARCHIVE, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for file in os.listdir(FILES_PATH):
            zip_file.write(os.path.join(FILES_PATH, file), file, compress_type=zipfile.ZIP_DEFLATED)

    yield

    shutil.rmtree(ARCHIVE)