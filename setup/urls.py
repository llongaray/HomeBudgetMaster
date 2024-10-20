from django.contrib import admin
from django.urls import path, include  # Importar include para incluir URLs de outros apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('financeiro.urls')),  # Inclui as URLs do app financeiro
]
