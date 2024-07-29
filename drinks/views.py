from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def drink_list(request, format=None):
    
    # get all the drinks
    # serialize them
    # return json
    
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response({'drink': serializer.data})
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'drink': serializer.data},status=status.HTTP_201_CREATED)
    
    
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, pk, format=None):
    
    # get the drink with id=pk
    # serialize it
    # return json
    
    try:
      drink = Drink.objects.get(pk=pk)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
       serializer = DrinkSerializer(drink)
       return Response({'drink': serializer.data})
            
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'drink': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    