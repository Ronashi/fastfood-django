from django.shortcuts import render
from .models import Pizza, Burger


def index(request):
    return render(request, 'food/index.html')

def pizza(request):
    pizzas = Pizza.objects.all()
    context =  {'pizzas': pizzas}
    print(pizzas)
    return render(request, 'food/pizza.html', context)


# def burger(request):
#     return render(request, 'food/burger.html')
