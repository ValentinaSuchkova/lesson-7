import os.path

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
FILES_PATH = os.path.join(CURRENT_DIR, 'files')
ARCHIVE_PATH = os.path.abspath('source')
ARCHIVE = os.path.join(ARCHIVE_PATH, 'archive.zip')