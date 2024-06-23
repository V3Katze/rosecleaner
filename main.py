# -*- coding: utf-8 -*-

import os
import requests
import sys
import shutil

SCRIPT_URL = "https://raw.githubusercontent.com/V3Katze/rosecleaner/main/main.py"
SCRIPT_PATH = os.path.abspath(__file__)

def download_latest_version():
    try:
        response = requests.get(SCRIPT_URL)
        response.raise_for_status()

        with open("main.py", 'w', encoding='utf-8') as out_file:
            out_file.write(response.text)

        print("Neueste Version heruntergeladen.")
        return True
    except Exception as e:
        print(f"Fehler beim Herunterladen der neuesten Version: {e}")
        return False

if __name__ == "__main__":
    download_latest_version()
    print("Niggerchen...")
