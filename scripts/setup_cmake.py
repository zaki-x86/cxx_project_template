# Needs: os, version, out_name

import sys
import requests
from os.path import abspath
from os.path import basename as path_basename
from subprocess import run as execute_process
from detect_os import detect_os
from detect_os import detect_os


from argparse import ArgumentParser, Namespace
def parse_cmd_args() -> Namespace:
    # Create an ArgumentParser object
    parser = ArgumentParser(description='Setup CMake')

    # Add arguments to the parser
    parser.add_argument('--version', type=str, help='CMake version', required=True)
    parser.add_argument('--out-name', type=str, help='output file name', required=False)

    # Parse the command-line arguments
    args = parser.parse_args()
    return args

def get_url(_version) -> str:
    if(_os == "windows"):
        cmake_suffix = "windows-x86_64.zip"
        cmake_dir = "cmake-${_version}-windows-x86_64/bin"
    elif(_os == "unix"):
        cmake_suffix = "linux-x86_64.tar.gz"
        cmake_dir = "cmake-${_version}-linux-x86_64/bin"
    elif(_os == "macos"):
        cmake_suffix = "macos-universal.tar.gz"
        cmake_dir = "cmake-${_version}-macos-universal/CMake.app/Contents/bin"
    else:
        exit(1)

    return f"https://github.com/Kitware/CMake/releases/download/v{_version}/cmake-{_version}-{cmake_suffix}"

from tqdm import tqdm
from urllib.parse import urlsplit
def download(url, _out_name="") -> str:
    if(not _out_name):
        path = urllib.parse.urlsplit(url).path
        _out_name = os.path.basename(path)
    
    response = requests.get(url, stream=True)
    
    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024  # 1 Kibibyte

    with open(_out_name, "wb") as f:
        for data in tqdm(response.iter_content(block_size), total=total_size // block_size, unit='KB', unit_scale=True):
            f.write(data)
    print("Download complete!")
    return _out_name
    
def extract( arcv_path : str, dest_path : str ="." ) -> str:
    completed = execute_process(["tar", "xvf", arcv_path, "-C", abspath(dest_path)])
    if completed.returncode == 0:
        print("Done")
    return abspath(dest_path)

if __name__ == "__main__":
    
    _os = detect_os()
    args = parse_cmd_args()
    _version = args.version
    _out_name = args.out_name 
    print(f"Downloading version {_version} on {_os}")
    
    url = get_url(_version)
    print(f"Download url: {url}")
    
    # Usually when you download from a url, such as: "https://website.come/downloads/releases/softwarev1.0"
    # The downloaded archive has the basename of the url, which is: "softwarev1.0"
    # Function download, returns the basename of the url 
    out_arcv = download(url)
    print(f"Downloaded file: {out_arcv}")
    
    out_arcv = extract(out_arcv)
    print(f"Path to output archive: {out_arcv}")
    