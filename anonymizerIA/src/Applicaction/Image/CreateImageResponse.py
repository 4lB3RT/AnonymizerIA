from anonymizerIA.src.Domain.Image.Image import Image

class CreateImageResponse(): 
    def __init__(self, image: Image) -> None:
        self.__image = image  
        
    def image(self) -> Image: 
        return self.__image