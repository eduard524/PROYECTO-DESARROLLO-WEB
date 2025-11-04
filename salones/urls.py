
from django.urls import path
from .views import SalonList, SalonCreate, SalonUpdate, SalonDelete

app_name = "salones"

urlpatterns = [
    path("", SalonList.as_view(), name="list"),
    path("nuevo/", SalonCreate.as_view(), name="create"),
    path("<int:pk>/editar/", SalonUpdate.as_view(), name="update"),
    path("<int:pk>/eliminar/", SalonDelete.as_view(), name="delete"),
]
