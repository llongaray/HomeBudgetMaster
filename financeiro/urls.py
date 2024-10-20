from django.urls import path
from .views import *  # Certifique-se de que suas views estão importadas

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('all_forms/', render_all_forms, name='all_forms'),
]

