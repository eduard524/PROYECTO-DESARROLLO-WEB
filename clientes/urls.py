from django.urls import path
from .views import ClienteList, ClienteCreate, ClienteUpdate, ClienteDelete

app_name = "clientes"

urlpatterns = [
    path("", ClienteList.as_view(), name="list"),
    path("nuevo/", ClienteCreate.as_view(), name="create"),
    path("<int:pk>/editar/", ClienteUpdate.as_view(), name="update"),
    path("<int:pk>/eliminar/", ClienteDelete.as_view(), name="delete"),
]
