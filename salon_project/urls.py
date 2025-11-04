from django.contrib import admin
from django.urls import path, include
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),

    
    path('', main_views.dashboard, name='home'),
    path('dashboard/', main_views.dashboard, name='dashboard'),

    
    path("clientes/", include("clientes.urls")),
    path("salones/", include("salones.urls")),
    path("reservas/", include("reservas.urls")),
    path("servicios/", include("servicios.urls")),
    path("pagos/", include("pagos.urls")),
]
