# Needs: os, version, out_name

import sys
import os
import requests
from tqdm import tqdm
import subprocess
from argparse import ArgumentParser, Namespace
from detect_os import detect_os
import urllib.parse
import tarfile


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
    
def extract(arcv_name, dest_dir=".") -> str:
    subprocess.run(["tar", "-xzvf", arcv_name, "-C", dest_dir])

if __name__ == "__main__":
    args = parse_cmd_args()
    _os = detect_os()
    _version = args.version
    _out_name = args.out_name    
    
    url = get_url(_version)
    
    # Usually when you download from a url, such as: "https://website.come/downloads/releases/softwarev1.0"
    # The downloaded archive has the basename of the url, which is: "softwarev1.0"
    # Function download, returns the basename of the url 
    out_arcv = download(url)
    out_arcv = extract(out_arcv)
    