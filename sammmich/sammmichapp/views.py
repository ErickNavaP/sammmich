from django.shortcuts import render
from django.http import Http404
from django.views import View
import random

# Create your views here.

ingredients = {
    'meats': ['corned beef', 'pastrami', 'honey turkey', 'pepper steak', 'veggie burger'],
    'cheeses': ['american', 'swiss', 'provolone', 'cheddar', 'mozzarella'],
    'toppings': ['lettuce', 'tomato', 'onions', 'peppers', 'pickles']
}

class SammmichappView(View):
    def get(self, request):
        return render (
            request = request,
            template_name = 'sammmichapp.html',
            context = {'ingredients': ingredients.keys()}
             ) 


    
class IngredientsView(View):
    def get(self, request, ingredient_type):
        if ingredient_type not in ingredients:
            raise Http404(f'No such ingredient: {ingredient_type}')

        return render (
            request = request,
            template_name = "ingredients_list.html",
            context = {
                'ingredients': ingredients[ingredient_type],
                'ingredient_type': ingredient_type,}
            
        )

class SammmichGeneratorView(View):
    def get(self, request):
        selected_meat = random.choice(ingredients['meats'])
        selected_cheese = random.choice(ingredients['cheeses'])
        selected_toppings = random.choice(ingredients['toppings'])

        sammmich = f'{selected_meat} & {selected_cheese} with {selected_toppings}'
        return render(request, 'sammmich_generator.html', context = {'sammmich' : sammmich})


class MenuView(View):    
    def get(self, request):
        return render(
            request, 
            "menu.html",
            context={
                "meats": ingredients["meats"],
                "cheeses": ingredients["cheeses"],
                "toppings": ingredients["toppings"],
            }
        )  
        