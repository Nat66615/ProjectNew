from rest_framework import generics
from .models import Product
from .serializers import MyproductSerialize

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



# Create your views here.
class MyModelView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = MyproductSerialize

class MyModelDetails(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = MyproductSerialize

class ObtainToken(APIView):
    def post(self, request):
        user = request.user
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
