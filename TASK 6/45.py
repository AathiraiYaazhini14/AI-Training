class Engine:
    def run(self, plugin):
        plugin.execute()

class Plugin:
    def execute(self):
        print("Plugin Running")

Engine().run(Plugin())
