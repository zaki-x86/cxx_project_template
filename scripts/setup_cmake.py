# Needs: os, version, out_name

import sys
import requests
from os.path import abspath, join as join_path
from os import extsep as os_extsep, mkdir
from os.path import basename as path_basename
from subprocess import run as execute_process
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
    _os = detect_os()
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
 
    
if __name__ == "__main__":
    
    _os = detect_os()
    args = parse_cmd_args()
    _version = args.version
    _out_name = args.out_name 
    #print(f"Downloading version {_version} on {_os}")
    
    url = get_url(_version)
    #print(f"Download url: {url}")
    
    # Usually when you download from a url, such as: "https://website.come/downloads/releases/softwarev1.0"
    # The downloaded archive has the basename of the url, which is: "softwarev1.0"
    # Function download, returns the basename of the url 
    out_arcv = download(url)
    #print(f"Downloaded file: {out_arcv}")
    
    print(out_arcv, file=sys.stdout)
    
    