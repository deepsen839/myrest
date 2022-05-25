from rest_framework import serializers
from .models import Dog,Breed
class breedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'  

class custombreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('id','name',)  


class dogsforgetSerializer(serializers.ModelSerializer):
    breed = custombreedSerializer(read_only=True)
    class Meta:
        model = Dog
        fields = '__all__'

class dogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'
      

    
