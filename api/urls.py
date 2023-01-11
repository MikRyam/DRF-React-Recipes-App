from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('recipes/', views.getRecipes, name="recipes"),
    path('categories/', views.getCategories, name="categories"),
    path('categories/<int:pk>/', views.getCategory, name="category"),
    path('recipes/<str:slug>/', views.getRecipe, name="recipe"),
]