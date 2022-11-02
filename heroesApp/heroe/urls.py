# Django import
from django.urls import path 

# Views. Las views son clases. Estamos importando una clase basicamente
from heroe.views import (
    HeroApiView, 
    CreateHeroeApiView, 
    HeroeDetailApiView,
    hero_api_view,
    hero_detail_api_view
    )

# Urls
urlpatterns = [
    path('heroe-list/', HeroApiView.as_view(), name='heroe_list'),
    path('list-hero/', hero_api_view, name='list'),
    path('create-heroe/', CreateHeroeApiView.as_view(), name='create'),
    # Se debe indicar el parametro que esperamos 
    path('detail-heroe/<int:pk>/', HeroeDetailApiView.as_view(), name='detail'),
    path('hero-detail/<int:pk>/', hero_detail_api_view, name='hero-detail'),
    
]
