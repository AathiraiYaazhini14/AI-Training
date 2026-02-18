from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    def execute(self):
        pass

class MyPlugin(Plugin):
    def execute(self):
        print("Plugin Running")

MyPlugin().execute()
