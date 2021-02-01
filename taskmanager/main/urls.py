from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('about', views.about, name='about'),
    path('pes', views.pes, name='pes'),
    path('pidor', views.pidor, name='pidor'),
    path('dog', views.dog, name='dog'),
    path('sobaka', views.sobaka, name='sobaka'),
    

]
