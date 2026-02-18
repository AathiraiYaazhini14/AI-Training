import platform
import sys

if platform.system() != "Windows":
    sys.exit()

print("Environment OK")
