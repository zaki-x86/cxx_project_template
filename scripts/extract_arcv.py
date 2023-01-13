import sys
from os.path import abspath, splitext, join as join_path
from os import extsep as os_extsep, mkdir
from os.path import basename as path_basename
from tarfile import open as tar_open
import zipfile
import signal

def timeout_handler(signum, frame):
    raise TimeoutError("Input timeout")

from argparse import ArgumentParser, Namespace

def parse_cmd_args() -> Namespace:
    # Create an ArgumentParser object
    parser = ArgumentParser(description='Download CMake')

    # Add arguments to the parser
    parser.add_argument('--arcv_path', type=str, help='path, or name of the archieve to uncompress', required=False)
    parser.add_argument('--dest_path', type=str, help='path to uncompress, default is cwd which behaves similar to extract_here option in GUI', required=False)

    # Parse the command-line arguments
    args = parser.parse_args()
    return args


def extract_here( arcv_path : str ) -> str:
    # Creates a new directory matches same name as archive
    # Extracts all contents to that directory
    # Returns the path to the created directory

    dest_path = "."
    fname = path_basename(arcv_path)    
    
    if fname.endswith("tar.gz"):
        dir_name = abspath(fname.replace(f"{os_extsep}tar.gz", ""))

    elif fname.endswith("tar"):
        dir_name = abspath(fname.replace(f"{os_extsep}tar", ""))
    elif fname.endswith("zip"):
        dir_name = abspath(fname.replace(f"{os_extsep}zip", ""))
    else:
        return None
    
    try:
        mkdir(join_path(dest_path, dir_name))
        dest_path = abspath(dir_name)
    except FileExistsError:
        print("Invalid, file already exists", file=sys.stderr)
        exit(1)
    
    if fname.endswith("tar.gz"):
        tar = tar_open(fname, "r:gz")
        #members  = tar.getmembers()
        tar.extractall(path=dest_path)
        tar.close()
        
    elif fname.endswith("tar"):
        tar = tar_open(fname, "r:")
        #members  = tar.getmembers()
        tar.extractall(path=dest_path)
        tar.close()
        
    elif fname.endswith("zip"):
        with zipfile.ZipFile(fname, 'r') as zip_ref:
            zip_ref.extractall(path=dest_path)
    
    # directories = [dir.name for dir in members if dir.isdir()]
    # files = [f.name for f in members if f.isfile()]
    return dest_path

def exteract_to( arcv_path : str, dest_path : str ) -> str:
    
    fname = path_basename(arcv_path)
    
    if fname.endswith("tar.gz"):
        tar = tar_open(fname, "r:gz")
        #members  = tar.getmembers()
        tar.extractall(path=dest_path)
        tar.close()
        
    elif fname.endswith("tar"):
        tar = tar_open(fname, "r:")
        #members  = tar.getmembers()
        tar.extractall(path=dest_path)
        tar.close()
        
    elif fname.endswith("zip"):
        with zipfile.ZipFile(fname, 'r') as zip_ref:
            zip_ref.extractall(path=dest_path)
    
    # directories = [dir.name for dir in members if dir.isdir()]
    # files = [f.name for f in members if f.isfile()]
    return dest_path


if __name__ == "__main__":
    
    args = parse_cmd_args()
    in_arcv = args.arcv_path
    
    if(not in_arcv):
        # Set the alarm for 5 seconds to wait for input
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(5)
        try:
            in_arcv = input()
            signal.alarm(0)
            #print(f"Received archive name: {in_arcv}")
            if(args.dest_path):
                out = exteract_to(in_arcv, args.dest_path)
            else:
                out = extract_here(in_arcv)
            print(out, file=sys.stdout)
            exit(0)
        except TimeoutError:
            print("Input timeout, Exiting", file=sys.stderr)
            print("Can't proceed without a path to the archive name", file=sys.stderr)
            exit(1)
    
    if(args.dest_path):
        out = exteract_to(args.arcv_path, args.dest_path)
    else:
        out = extract_here(args.arcv_path)