from django.urls import path
from . import views

urlpatterns = [
    path('login', views.auth, name='auth'),
    path('', views.index, name='index'),
    path('<int:id>', views.show, name='show'),
]