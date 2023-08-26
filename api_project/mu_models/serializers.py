from rest_framework import serializers
from .models import A

class MyproductSerialize(serializers.ModelSerializer):
    class Meta:
        model = A
        #fields = '__all__'
        fields = ['id', 'price']