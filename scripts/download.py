import requests
from os import path
from tqdm import tqdm
from urllib.parse import urlsplit

def download( url : str, _out_name : str ="" ) -> str:
    if(not _out_name):
        path = urlsplit(url).path
        _out_name = path.basename(path)
        
    response = requests.get(url, stream=True)

    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024  # 1 Kibibyte

    with open(_out_name, "wb") as f:
        for data in tqdm(response.iter_content(block_size), total=total_size // block_size, unit='KB', unit_scale=True):
            f.write(data)
    
    return path.abspath(_out_name)