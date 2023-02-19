class Image:
    def __init__(self, name:str, description: str, size: str, url: str|None):
        self.__name = name
        self.__description = description
        self.__size = size
        self.__url = url

    def name(self) -> str:
        return self.__name
    
    def description(self) -> str:
        return self.__description
    
    def url(self) -> str|None:
        return self.__url
    
    def updateUrl(self, url: str) -> None:
        self.__url = url
    
    def size(self) -> str:
        return self.__size