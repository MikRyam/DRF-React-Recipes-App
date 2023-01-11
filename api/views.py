from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Category, Recipe
from .serializers import CategorySerializer, RecipeSerializer


# Create your views here.

@api_view(['GET'])
def getRoutes(request):
      routes = [
        {
            'Endpoint': '/recipes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of recipes'
        },
        {
            'Endpoint': '/categories/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of categories'
        },
        {
            'Endpoint': '/categories/id/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of a single category recipes'
        },
        {
            'Endpoint': '/recipes/id/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single recipe'
        },
      ]
      return Response(routes)
      

@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRecipes(request):
    categories = Recipe.objects.all()
    serializer = RecipeSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCategory(request, pk):
    recipes = Recipe.objects.filter(category_id=pk)
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRecipe(request, slug):
    recipe = Recipe.objects.get(slug=slug)
    serializer = RecipeSerializer(recipe, many=False)
    return Response(serializer.data)
