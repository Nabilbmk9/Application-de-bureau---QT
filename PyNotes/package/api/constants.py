import os
from pathlib import Path

current_dir = Path(__file__).parent.parent.parent
NOTES_DIR = os.path.join(current_dir, ".notes")