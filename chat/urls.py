from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name = 'home'),
    path('group/<int:id>', group, name = 'group'),
    path('comment/<int:id>', comment, name='comment'),
]