import requests
from os import path
from tqdm import tqdm
from urllib.parse import urlsplit

from argparse import ArgumentParser, Namespace

def parse_cmd_args() -> Namespace:
    # Create an ArgumentParser object
    parser = ArgumentParser(description='Setup CMake')

    # Add arguments to the parser
    parser.add_argument('--url', type=str, help='File url to download', required=True)

    # Parse the command-line arguments
    args = parser.parse_args()
    return args

def download( url : str, _out_name : str ="" ) -> str:
    if(not _out_name):
        _path = urlsplit(url).path
        _out_name = path.basename(_path)
        
    response = requests.get(url, stream=True)

    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024  # 1 Kibibyte

    with open(_out_name, "wb") as f:
        for data in tqdm(response.iter_content(block_size), total=total_size // block_size, unit='KB', unit_scale=True):
            f.write(data)
    
    return path.abspath(_out_name)

if __name__ == "__main__":
    args = parse_cmd_args()
    download(args.url)