from django.contrib import admin
from django.urls import path, include  # Importe include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('payments.urls')),  # Inclua as URLs da sua API aqui
]
