from django.shortcuts import render
from myapp.models import Dog,Breed
from myapp.serializers import breedSerializer,dogsSerializer,dogsforgetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class DogList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Dog.objects.all()
        serializer = dogsforgetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = dogsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dogs = self.get_object(pk)
        serializer = dogsforgetSerializer(dogs)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dogs = self.get_object(pk)
        serializer = dogsSerializer(dogs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            dogs = self.get_object(pk)
            serializer = dogsforgetSerializer(dogs)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dogs = self.get_object(pk)
        dogs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Breed.objects.all()
        serializer = breedSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = breedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BreedDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        breed = self.get_object(pk)
        serializer = breedSerializer(breed)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        breed = self.get_object(pk)
        serializer = breedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        breed = self.get_object(pk)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


