import os
from detect_os import detect_os

GITHUB_WORKSPACE = os.environ.get('GITHUB_WORKSPACE')
GITHUB_PATH = os.environ.get('GITHUB_PATH')

def export_to_github_env(path):
    if detect_os() == "windows":
        path_seprator = ";"
    elif detect_os() == "unix" | detect_os() == "macos":
        path_seprator = ":"