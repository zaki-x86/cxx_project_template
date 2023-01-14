import subprocess
from os import environ, path

from detect_os import detect_os
from setup_cmake import get_url as get_cmake_url
from setup_ninja import get_url as get_ninja_url
from extract_arcv import extract_here
from github_env import GITHUB_WORKSPACE, GITHUB_PATH, RUNNER_OS
from download import download
from command_runner import command

CMAKE_VERSION = environ.get('CMAKE_VERSION')
NINJA_VERSION = environ.get('NINJA_VERSION')


print(f"Detected OS: {RUNNER_OS})")
# See Github enviroment variables
print("Enviroment: ")
subprocess.run(["env"])

"""Notes
* get_cmake_url(version : str) -> str and get_ninja_url(version : str) -> str:
puts together the url used to download cmake and ninja respectively

* download(url : str) -> str 
downloads cmake and ninja then it outputs the absolute path of the downloaded archive.

* extract_here(compressed_file : str) -> str:
behaves similar the GUI `extract here` in ubuntu, and it outputs the absolute path to the extracted content

* command(cmd:str):
is just an abstraction for the function: subprocess.run(cmd, shell=True)
"""

# 
# extract_here
print(f"Downloading CMake v{CMAKE_VERSION}")
url = get_cmake_url(CMAKE_VERSION)
print(f"CMake Download URL: {url}")
cmake_out_arcv = download(url)
print(f"Downloaded: {cmake_out_arcv}")

print(f"Extracting {cmake_out_arcv}: ")
cmake_dir = extract_here(cmake_out_arcv)
print(f"Extracted: {cmake_dir}")

if RUNNER_OS == "Windows":
    cmake_dir = f"cmake-{CMAKE_VERSION}-windows-x86_64/ cmake-{CMAKE_VERSION}-windows-x86_64/bin"
elif RUNNER_OS == "Linux":
    cmake_dir = f"cmake-{CMAKE_VERSION}-linux-x86_64/cmake-{CMAKE_VERSION}-linux-x86_64/bin"
elif RUNNER_OS == "macOS":
    cmake_dir = f"cmake-{CMAKE_VERSION}-macos-universal/cmake-{CMAKE_VERSION}-macos-universal/CMake.app/Contents/bin"
    
cmake_dir = path.join(GITHUB_WORKSPACE, cmake_dir)

# -------------------

print(f"Downloading Ninja v{NINJA_VERSION}")
ninja_url = get_ninja_url(NINJA_VERSION)
print(f"Ninja Download URL: {ninja_url}")
ninja_out_arcv = download(ninja_url)
print(f"Downloaded: {ninja_out_arcv}")

print(f"Extracting {ninja_out_arcv}: ")
ninja_dir = extract_here(ninja_out_arcv)
print(f"Extracted: {ninja_dir}")

if RUNNER_OS != "Windows":
    # Exports both ninja_dir and cmake_dir
    #command(f'echo "{ninja_dir}:{cmake_dir}" >> $GITHUB_PATH ')
    command(f"chmod +x {ninja_dir}/ninja")
    command(f"chmod +x {cmake_dir}/cmake")
    
