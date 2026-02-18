from abc import ABC, abstractmethod

class Processor(ABC):
    @abstractmethod
    def process(self):
        pass

class TextProcessor(Processor):
    def process(self):
        print("Text Processing")

class ImageProcessor(Processor):
    def process(self):
        print("Image Processing")

for p in [TextProcessor(), ImageProcessor()]:
    p.process()
