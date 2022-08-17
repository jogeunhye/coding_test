from django.urls import path, include
from . import views


app_name = 'board'

urlpatterns =[
    path('new', views.new, name='new'),
]