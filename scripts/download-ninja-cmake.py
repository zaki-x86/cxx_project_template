import subprocess
from os import environ, path

from detect_os import detect_os
from setup_cmake import get_url as get_cmake_url
from setup_ninja import get_url as get_ninja_url
from extract_arcv import extract_here
from github_env import GITHUB_WORKSPACE, GITHUB_PATH, export_to_github_env
from download import download
from command_runner import command

CMAKE_VERSION = environ.get('CMAKE_VERSION')
NINJA_VERSION = environ.get('NINJA_VERSION')
RUNNING_OS = detect_os()

print(f"Detected OS: {RUNNING_OS})")
# See Github enviroment variables
print("Enviroment: ")
subprocess.run(["env"])

print(f"Downloading CMake v{CMAKE_VERSION}")
url = get_cmake_url(CMAKE_VERSION)
print(f"CMake Download URL: {url}")
cmake_out_arcv = download(url)
print(f"Downloaded: {cmake_out_arcv}")

print(f"Extracting {cmake_out_arcv}: ")
cmake_dir = extract_here(cmake_out_arcv)
print(f"Extracted: {cmake_dir}")

command(f"ls {cmake_dir}")

print("Exporting CMake path: ")
if RUNNING_OS == "windows":
    cmake_dir = f"cmake-{CMAKE_VERSION}-windows-x86_64/bin"
elif RUNNING_OS == "unix":
    cmake_dir = f"cmake-{CMAKE_VERSION}-linux-x86_64/bin"
elif RUNNING_OS == "macos":
    cmake_dir = f"cmake-{CMAKE_VERSION}-macos-universal/CMake.app/Contents/bin"
    
cmake_dir = path.join(GITHUB_WORKSPACE, cmake_dir)
export_to_github_env(cmake_dir)

if RUNNING_OS != "windows":
    command(f"chmod +x {cmake_dir}/cmake")

print("Testing CMake installation: ")
command("cmake --version")
# -------------------

print(f"Downloading Ninja v{NINJA_VERSION}")
ninja_url = get_ninja_url(NINJA_VERSION)
print(f"Ninja Download URL: {ninja_url}")
ninja_out_arcv = download(ninja_url)
print(f"Downloaded: {ninja_out_arcv}")

print(f"Extracting {ninja_out_arcv}: ")
ninja_dir = extract_here(ninja_out_arcv)
print(f"Extracted: {ninja_dir}")

ninja_dir = path.join(GITHUB_WORKSPACE, ninja_dir)
# todo: edit cmake_dir to be path to binary
export_to_github_env(ninja_dir)

#if RUNNING_OS != "windows":
#    command(f"chmod +x {ninja_dir}/ninja")
    
#print("Testing Ninja installation: ")
#command("ninja --version")

if RUNNING_OS == "unix":
    command("sudo apt install tree")
    command("tree -L 3")