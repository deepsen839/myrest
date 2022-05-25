from rest_framework import serializers
from .models import Dog,Breed
class breedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'  
class dogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'
      

    
