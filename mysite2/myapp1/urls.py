from django.urls import path, include
from . import views

app_name = 'myapp1'

urlpatterns = [
    path('', views.index, name='index'),
    path('party/', views.party, name='party'),
    path('leader/', views.leader, name='leader'),
]
