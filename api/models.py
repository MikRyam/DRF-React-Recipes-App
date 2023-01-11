from django.db import models

# Create your models here.

# class Recipe(models.Model):
#     SALADS = 'salads'
#     APPETIZERS = 'appetizers'
#     SOUPS = 'soups'
#     MAIN_COURSE = 'main course'
#     DESSERT = 'dessert'  

#     CATEGORIES = [
#         (SALADS, 'salads'),
#         (APPETIZERS, 'appetizers'),
#         (SOUPS, 'soups'),
#         (MAIN_COURSE, 'main course'),
#         (DESSERT, 'dessert'),      
#     ]

#     title = models.CharField('Title', max_length=128)
#     ingredients = models.TextField('Ingredients', null=True, blank=True)
#     instructions = models.TextField('Instructions', null=True, blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     category = models.CharField(max_length=20, choices=CATEGORIES, default=SALADS)

#     def __str__(self):        
#         return f'{self.category}  |  {self.title}'

#     def get_categories():
#         cat_menu = [
#         'salads',
#         'soups',
#         'main course',
#         'dessert',
#       ]
#         return cat_menu


class Category(models.Model):
    SALADS = 'САЛАТЫ'
    APPETIZERS = 'ЗАКУСКИ'
    SOUPS = 'СУПЫ'
    MAIN_COURSE = 'ГОРЯЧЕЕ'
    DESSERT = 'ДЕСЕРТЫ'  

    CATEGORIES = [
        (SALADS, 'САЛАТЫ'),
        (APPETIZERS, 'ЗАКУСКИ'),
        (SOUPS, 'СУПЫ'),
        (MAIN_COURSE, 'ГОРЯЧЕЕ'),
        (DESSERT, 'ДЕСЕРТЫ'),      
    ]

    name = models.CharField(max_length=20, choices=CATEGORIES, default=SALADS)
    slug = models.SlugField(max_length=20, default='salads')

    def __str__(self):        
        return f'{self.name}'

    def get_categories():
        cat_menu = [
        'salads',
        'soups',
        'main course',
        'dessert',
      ]
        return cat_menu

class Recipe(models.Model):

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField('Title', max_length=128)
    ingredients = models.TextField('Ingredients', null=True, blank=True)
    instructions = models.TextField('Instructions', null=True, blank=True)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f'{self.category.name}  |  {self.title}'
