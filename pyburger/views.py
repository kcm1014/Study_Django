from django.shortcuts import render
from pyburger.models import Burger
# Create your views here.

def main(request):
    return render(request,"pyburger/main.html")

def burger_list(request):
    burgers = Burger.objects.all()
    context = {"burgers":burgers}
    return render(request,"pyburger/burger_list.html",context)

def burger_search(request):
    #print(request.GET)
    # print(keyword)
    keyword = request.GET.get('keyword')
    if keyword is None:
        burgers = Burger.objects.none()
    else:
        burgers = Burger.objects.filter(name__contains =keyword)
    #print(burgers)
    context = {'burgers':burgers}
    return render(request,"pyburger/burger_search.html",context)