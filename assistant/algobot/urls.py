from django.urls import path
from .views import ask_view

urlpatterns = [
    path('', ask_view, name='ask'),  # Updated to use the name 'ask' for the view
    path('ask/', ask_view),  # Updated to use the name 'ask' for the view
]
