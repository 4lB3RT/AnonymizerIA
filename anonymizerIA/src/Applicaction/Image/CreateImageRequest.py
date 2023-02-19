class CreateImageRequest(): 
    def __init__(self, description: str):
        self.__description = description  
        
    def description(self) -> str: 
        return self.__description