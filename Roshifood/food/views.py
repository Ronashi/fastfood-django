from django.shortcuts import render
from .models import pizza, burger


def index(request):
    return render(request, 'food/index.html')

def pizza(request):
    pizzas = pizzas.objects.all()
    context =  {'pizzas': pizzas}
    return render(request, 'food/pizza.html', context)

# def burger(request):
#     return render(request, 'food/burger.html')