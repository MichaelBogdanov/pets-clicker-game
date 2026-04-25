from django.urls import path
from .views import *

urlpatterns = [
    path('register/<str:login>/<str:password>', register),
    path('login/<str:login>/<str:password>', login),
    path('get_score/<str:login>', get_score),
    path('add_score/<str:login>/<int:value>', add_score),
    path('reduce_score/<str:login>/<int:value>', reduce_score),
    path('add_animal/<str:login>/<str:kind>', add_animal),
    path('get_animals/<str:login>', get_animals)
]
