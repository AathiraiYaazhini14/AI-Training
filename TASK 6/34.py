class Strategy:
    def respond(self):
        pass

class Friendly(Strategy):
    def respond(self):
        print("Hi")

class Formal(Strategy):
    def respond(self):
        print("Hello")

def chat(s):
    s.respond()

chat(Friendly())
chat(Formal())
