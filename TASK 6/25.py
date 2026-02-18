class Storage:
    def upload(self):
        pass

class AWS(Storage):
    def upload(self):
        print("AWS Upload")

class GCP(Storage):
    def upload(self):
        print("GCP Upload")

def process(s):
    s.upload()

process(AWS())
process(GCP())
