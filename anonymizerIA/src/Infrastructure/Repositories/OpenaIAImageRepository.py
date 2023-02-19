import os
import openai
from dotenv import load_dotenv
from anonymizerIA.src.Domain.Image.ImageRepository import ImageRepository
from anonymizerIA.src.Domain.Image.Image import Image

class OpenaIAImageRepository(ImageRepository):
    def __init__(self) -> None:
        load_dotenv()
        self.__openai = openai
        self.__openai.api_key = os.getenv("OPENAI_API_KEY")
    
    def create(self, image: Image) -> Image:
        response = self.__openai.Image.create(
            prompt = image.description(),
            n = 1,
            size = image.size()
        )
        
        url = response['data'][0]['url']
        image.updateUrl(url)
        
        return image
        