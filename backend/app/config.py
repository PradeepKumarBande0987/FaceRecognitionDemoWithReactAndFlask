"""Application configuration."""
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "instance", "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    STORAGE_FOLDER = os.path.join(BASE_DIR, "storage")
    REGISTERED_FACES_FOLDER = os.path.join(STORAGE_FOLDER, "registered_faces")
    TEMP_FRAMES_FOLDER = os.path.join(STORAGE_FOLDER, "temp_frames")
    ENCODINGS_FOLDER = os.path.join(STORAGE_FOLDER, "encodings")
    ENCODINGS_FILE = os.path.join(ENCODINGS_FOLDER, "encodings.pkl")
