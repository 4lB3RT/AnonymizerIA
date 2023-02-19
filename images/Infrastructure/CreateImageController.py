from django.http import HttpResponse, HttpRequest

class CreateImageController(): 
    def __index__(self, request: HttpRequest):    
        return HttpResponse("Foo says" , mimetype="text/plain")

         