from django.contrib import admin
from django.urls import path
from myapp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    # URL para a página principal
    path('', home, name='pagina_principal'),
]
