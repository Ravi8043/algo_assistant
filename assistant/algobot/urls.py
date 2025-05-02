from django.urls import path
from .views import ask_view, fine_tune_view

urlpatterns = [
    path('', ask_view, name='ask'), # Updated to use the name 'ask' for the view
    path('',fine_tune_view, name='fine_tune')
]
