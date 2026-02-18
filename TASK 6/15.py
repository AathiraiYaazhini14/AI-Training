import sys

class Logger:
    def __init__(self, supported):
        if sys.version_info[:2] not in supported:
            sys.exit()

Logger([(3,10),(3,11),(3,12)])
print("Environment Supported")
