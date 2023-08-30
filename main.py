import importlib
import json

import git_update_checker

main_file = "AutomationTool.py"
relative_path = "automation-tool-sensors-IP/"

# with open(relative_path+"config.json") as config_file:
#     files = json.load(config_file)[0]["files"]

# for f in files:
#     if f != main_file:
#         importlib.import_module(relative_path+f)
#     else:
#         main_file_import = importlib.import_module(relative_path+main_file)
# if hasattr(main_file_import,"__main__"):
#     main_func = getattr(main_file_import,"__main__")
#     main_func()

check_updates = getattr(git_update_checker,"__main__")
check_updates()


