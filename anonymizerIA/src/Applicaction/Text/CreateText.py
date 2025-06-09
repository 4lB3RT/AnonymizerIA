from anonymizerIA.src.Domain.Image.ImageRepository import ImageRepository
from anonymizerIA.src.Applicaction.Image.CreateImageRequest import CreateImageRequest
from anonymizerIA.src.Applicaction.Image.CreateImageResponse import CreateImageResponse
from anonymizerIA.src.Domain.Image.Image import Image


class CreateImage(): 
        
    def __init__(self, imageRepository: ImageRepository):
        self.__imageRepository = imageRepository
        pass
    
    def create(self, request: CreateImageRequest) -> CreateImageResponse:
        image = Image(
            "name",
            request.description(),
            "1024x1024",
            None
        )
        
        self.__imageRepository.create(image)
        
        return CreateImageResponse(image)
         