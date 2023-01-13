import sys

def detect_os():
    if sys.platform.startswith('win'):
        return "windows"
    elif sys.platform.startswith('linux'):
        return "unix"
    elif sys.platform.startswith('darwin'):
        return "macos"
    else:
        return "null" 

os = {"os" : detect_os()}

print(os)