from rest_framework import serializers
from .models import Dogs,Breeds
class breedSerialize(serializers.ModelSerializer):
    class Meta:
        model = Breeds
        fields = '__all__'  
class dogsSerialize(serializers.ModelSerializer):
    class Meta:
        model = Dogs
        fields = '__all__'
      

    
