from rest_framework import serializers
from .models import Dogs,Breeds
class breedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breeds
        fields = '__all__'  
class dogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dogs
        fields = '__all__'
      

    
