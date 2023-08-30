import os
import requests
import json
from dotenv import load_dotenv
import tkinter as tk
import tkinter.messagebox as mb


def __main__():
    root = tk.Tk()
    root.withdraw()

    load_dotenv()

    user = os.getenv("USER")
    token = os.getenv("TOKEN")
    url = os.getenv("URL")

    repo = "automation-tool-sensors-IP"

    with open("automation-tool-sensors-IP/config.json") as config_file:
        current_version = str(json.load(config_file)[0]["version"])
    current_version = "4.2"

    response = requests.get(url)
    data = response.json()

    latest_version = str(data["files"]["gistfile1.txt"]["content"].split(repo+" : ")[1])
    print(f"Latest Version: {latest_version}")


    if latest_version != current_version:
        user_response = mb.askokcancel("Update Available",f"There is an available update from version {current_version} to version {latest_version}. Do you want to proceed?")

    print(f"User response: {user_response}")

    if user_response: 
        print("Kill the main process.")

        repo_url = f"https://raw.githubusercontent.com/ulbios/{repo}/master/AutomationTool.py"

        download = requests.get(repo_url,auth=(user,token)).content
        with open("new_file.py","wb") as f:
            f.write(download)
        pass

if __name__ == "__main__":
    __main__()