from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from django.views.decorators.csrf import csrf_exempt
from anonymizerIA.src.Applicaction.Image.CreateImage import CreateImage, CreateImageRequest
from anonymizerIA.src.Infrastructure.Repositories.OpenaIAImageRepository import OpenaIAImageRepository

class CreateImageController(APIView):    

    def __init__(self, *args, **kwargs) -> None:
        self.__createImage = CreateImage(OpenaIAImageRepository())

    @csrf_exempt
    def post(self, request: Request, *args, **kwargs) -> Response:
        createImageRequest = CreateImageRequest(
            request.query_params.get("description")
        )
                        
        response = self.__createImage.create(createImageRequest)
        return  Response(status=200, data=response.image().url())


         