from abc import abstractmethod

from anonymizerIA.src.Domain.Image.Image import Image

class ImageRepository():
    @abstractmethod
    def find() -> Image:
        pass