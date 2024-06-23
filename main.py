import os,sys
import requests


SCRIPT_URL = "https://deinserver.com/latest_version.py"
SCRIPT_PATH = os.path.abspath(__file__)

def check_for_update():
    try:
        response = requests.get(SCRIPT_URL)
        response.raise_for_status()

        latest_script = response.text

        with open(SCRIPT_PATH, 'r') as current_file:
            current_script = current_file.read()

        if current_script != latest_script:
            with open(SCRIPT_PATH, 'w') as current_file:
                current_file.write(latest_script)
            print("Das Skript wurde aktualisiert. Starte es neu.")
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            print("Das Skript ist auf dem neuesten Stand.")
    except Exception as e:
        print(f"Fehler beim Überprüfen auf Updates: {e}")

if __name__ == "__main__":
    check_for_update()
    print("Updatet version...")
