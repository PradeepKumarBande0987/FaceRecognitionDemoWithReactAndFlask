"""File utility helpers."""
import os

def ensure_folder_exists(folder_path):
    os.makedirs(folder_path, exist_ok=True)
