# -*- coding: utf-8 -*-

import os
import requests
import sys
import shutil

# URL zur neuesten Version des Hauptskripts
SCRIPT_URL = "https://raw.githubusercontent.com/V3Katze/rosecleaner/main/main.py"
SCRIPT_PATH = os.path.abspath(__file__)

def download_latest_version():
    try:
        response = requests.get(SCRIPT_URL)
        response.raise_for_status()

        with open("latest_version.py", 'w', encoding='utf-8') as out_file:
            out_file.write(response.text)

        print("Neueste Version heruntergeladen.")
        return True
    except Exception as e:
        print(f"Fehler beim Herunterladen der neuesten Version: {e}")
        return False

def replace_and_restart():
    try:
        if os.path.exists("latest_version.py"):
            os.remove(SCRIPT_PATH)
            os.rename("latest_version.py", SCRIPT_PATH)
            print("Das Hauptskript wurde aktualisiert. Starte es neu.")
            os.execl(sys.executable, sys.executable, SCRIPT_PATH)
    except Exception as e:
        print(f"Fehler beim Ersetzen der Datei: {e}")

if __name__ == "__main__":
    if download_latest_version():
        replace_and_restart()
    else:
        # Der Hauptteil deines Skripts
        print("Updated...")
