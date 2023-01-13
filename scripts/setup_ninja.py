# Needs: os, version, out_name

import sys
import requests
from os.path import abspath
from os.path import basename as path_basename
from subprocess import run as execute_process


from argparse import ArgumentParser, Namespace
def parse_cmd_args() -> Namespace:
    # Create an ArgumentParser object
    parser = ArgumentParser(description='Setup Ninja')

    # Add arguments to the parser
    parser.add_argument('--version', type=str, help='Ninja version', required=True)
    parser.add_argument('--out-name', type=str, help='output file name', required=False)

    # Parse the command-line arguments
    args = parser.parse_args()
    
    return args


from detect_os import detect_os

def get_url( _version : str ) -> str:
    _os = detect_os()
    if(_os == "windows"):
        ninja_suffix = "win.zip"
    elif(_os == "unix"):
        ninja_suffix = "linux.zip"
    elif(_os == "macos"):
        ninja_suffix = "mac.zip"
    else:
        exit(1)
        
    url = f"https://github.com/ninja-build/ninja/releases/download/v${_version}/ninja-${ninja_suffix}"
    
    return url


from tqdm import tqdm
from urllib.parse import urlsplit

def download( url : str, _out_name : str ="" ) -> str:
    if(not _out_name):
        path = urlsplit(url).path
        _out_name = path_basename(path)
        
    response = requests.get(url, stream=True)

    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024  # 1 Kibibyte

    print("Downloading Ninja ...")


    with open(_out_name, "wb") as f:
        for data in tqdm(response.iter_content(block_size), total=total_size // block_size, unit='KB', unit_scale=True):
            f.write(data)

    print("Download complete!")
    
    return abspath(_out_name)

def extract( arcv_path : str, dest_path : str ) -> str:
    completed = execute_process(["tar", "xvf", arcv_path, -"C", abspath(dest_path)])
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
    
