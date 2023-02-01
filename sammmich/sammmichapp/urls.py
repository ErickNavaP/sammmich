from django.urls import path 
from sammmichapp.views import SammmichappView, IngredientsView, SammmichGeneratorView, MenuView

urlpatterns = [
    #sammmich/
    path('', SammmichappView.as_view(), name = 'sammmich'),
    #sammmich/ingredients/<str:ingredient_type>
    path('ingredients/<str:ingredient_type>', IngredientsView.as_view(), name = 'ingredients_list'),
    path('random', SammmichGeneratorView.as_view(), name='sammmich_generator'),
    path('menu/', MenuView.as_view(), name = 'menu')
    ]