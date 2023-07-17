from django.urls import path
from .views import index, cadastro

urlpatterns = [
    path('', index, name='index'),
    path('produto/<int:id>', cadastro, name='cadastro'),
]