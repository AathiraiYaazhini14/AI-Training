class Media:
    def play(self):
        pass

class MP3(Media):
    def play(self):
        print("Playing MP3")

class MP4(Media):
    def play(self):
        print("Playing MP4")

for m in [MP3(), MP4()]:
    m.play()
