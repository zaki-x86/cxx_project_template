import sys

def detect_os():
    if sys.platform.startswith('win'):
        return "windows"
    elif sys.platform.startswith('linux'):
        return "unix"
    elif sys.platform.startswith('darwin'):
        return "macos"
    else:
        return 

if __name__ == "__main__":
    print(detect_os())