import subprocess
from argparse import ArgumentParser, Namespace
import subprocess

def parse_cmd_args() -> Namespace:
    # Create an ArgumentParser object
    parser = ArgumentParser(description='Download CMake')

    # Add arguments to the parser
    parser.add_argument('--command', type=str, help='shell command', required=False)

    # Parse the command-line arguments
    args = parser.parse_args()
    return args


def command( cmd : str ):
    # Split the command string into a list of arguments
    try:
        # Run the command and capture the output
        output = subprocess.run(cmd, capture_output=True, check=True, shell=True)
        # Print the output
        print(output.stdout.decode())
    except subprocess.CalledProcessError as e:
        # Print the error message
        print(e.stderr.decode())
        
        
if __name__ == "__main__":
    args = parse_cmd_args()
    command(args.command)