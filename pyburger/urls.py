from django.urls import path
from pyburger.views import  main,burger_list,burger_search
urlpatterns = [
    path("",main),
    path("burgers/",burger_list),
    path('search/',burger_search),
]