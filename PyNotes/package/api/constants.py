import os
from pathlib import Path

current_dir = os.getcwd()
NOTES_DIR = os.path.join(current_dir, ".notes")


print(f"chemin = {NOTES_DIR}")