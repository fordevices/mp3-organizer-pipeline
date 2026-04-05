import os

INPUT_DIR = "Input"
OUTPUT_DIR = "Music"
DB_PATH = "music.db"
RUNS_DIR = "runs"
SUPPORTED_EXTENSIONS = [".mp3"]
SHAZAM_SLEEP_SEC = 2.0   # seconds to wait between ShazamIO calls
LANGUAGES = ["Tamil", "Hindi", "English", "Other"]

# AcoustID API key — register free at https://acoustid.org
ACOUSTID_API_KEY = os.getenv("ACOUSTID_API_KEY", "")

# Sarvam AI API key — register free at https://sarvam.ai
# Required only for the --transliterate pass
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY", "")
