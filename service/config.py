from pathlib import Path

current_file = Path(__file__).resolve()
PROJECT_ROOT = current_file.parent.parent #/dir1/dir2/config.py 

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw_json"
DATABASE_PATH = PROJECT_ROOT / "database" / "load_pulse.db"
ENV_PATH = PROJECT_ROOT / ".env"

#print(f"{DATABASE_PATH}")