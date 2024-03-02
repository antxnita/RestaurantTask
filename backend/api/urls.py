# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/<str:postcode>/', views.get_restaurants_by_postcode, name='get_restaurants_by_postcode'),
]






