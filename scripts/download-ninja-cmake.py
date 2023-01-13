import subprocess
from os import environ, path

from detect_os import detect_os
from setup_cmake import get_url, download
from extract_arcv import extract_here
from github_env import GITHUB_WORKSPACE, GITHUB_PATH, export_to_github_env

CMAKE_VERSION = environ.get('CMAKE_VERSION')
NINJA_VERSION = environ.get('NINJA_VERSION')
RUNNING_OS = detect_os()

print(f"Detected OS: {RUNNING_OS})")
# See Github enviroment variables
print("Enviroment: ")
subprocess.run(["env"])

print(f"Downloading CMake v{CMAKE_VERSION}")
url = get_url(CMAKE_VERSION)
print(f"CMake Download URL: {url}")
cmake_out_arcv = download(url)
print(f"Downloaded: {cmake_out_arcv}")

print(f"Extracting {cmake_out_arcv}: ")
cmake_dir = extract_here(cmake_out_arcv)
print(f"Extracted: {cmake_dir}")

subprocess.run(["ls", f"{cmake_dir}"])

print("Exporting CMake path: ")
cmake_dir = path.join(GITHUB_WORKSPACE, cmake_dir)
# todo: edit cmake_dir to be path to binary
export_to_github_env(cmake_dir)

print(f"Downloading Ninja v{NINJA_VERSION}")
url = get_url(NINJA_VERSION)
print(f"Ninja Download URL: {url}")
ninja_out_arcv = download(url)
print(f"Downloaded: {ninja_out_arcv}")

print(f"Extracting {ninja_out_arcv}: ")
ninja_dir = extract_here(ninja_out_arcv)
print(f"Extracted: {ninja_dir}")

subprocess.run(["ls", f"{ninja_dir}"])



