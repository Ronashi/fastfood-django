from django.shortcuts import render



def index(request):
    identify = {'name':'Ronashi', 'email':'Ronashi@gmail.com', 'msg':'have my way in this world'}
    return render(request, 'food/index.html', identify)

def pizza(request):
    return render(request, 'food/pizza.html')
