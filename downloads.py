import os
import shutil
from pathlib import Path

def download_organiser():
# File types categorised by extensions
    categories = {
        "Audio": ['.aif', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.wav', '.wma'],
        "Compressed": ['.7z', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z', '.zip'],
        "Code": ['.js', '.jsp', '.html', '.ipynb', '.py', '.java', '.css'],
        "Documents": ['.pdf', '.xls', '.xlsx', '.doc', '.docx', '.txt'],
        "Images": ['.bmp', '.gif', '.ico', '.jpeg', '.jpg', '.png', '.jfif', '.svg', '.tif', '.tiff'],
        "Software": ['.apk', '.bat', '.bin', '.exe', '.jar', '.msi', '.py'],
        "Videos": ['.3gp', '.avi', '.flv', '.h264', '.mkv', '.mov', '.mp4', '.mpg', '.mpeg', '.wmv'],
        "Other": []
    }

    # Assigning the root download folder
    home_dir = Path.home()
    download_root = home_dir / "Downloads"

    # Creation of folders for each category
    for category in categories:
        os.makedirs(os.path.join(download_root, category), exist_ok=True)

    # Organise files into the correct folder
    for file in os.listdir(download_root):
        file_path = os.path.join(download_root, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            DESTINATION = "Other"

            for category, extensions in categories.items():
                if ext in extensions:
                    DESTINATION = category
                    break
            FILE_MOVED = False

            shutil.move(file_path, os.path.join(download_root, DESTINATION, file))

