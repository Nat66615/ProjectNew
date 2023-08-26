from rest_framework import generics
from .models import A
from .serializers import MyproductSerialize


# Create your views here.
class MyModelView2(generics.ListAPIView):
    queryset = A.objects.all()
    serializer_class = MyproductSerialize