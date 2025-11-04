from django.urls import path
from .views import ReservaList, ReservaCreate, ReservaUpdate, ReservaDelete

app_name = "reservas"

urlpatterns = [
    path("",   ReservaList.as_view(),   name="list"),
    path("nueva/",  ReservaCreate.as_view(), name="create"),
    path("<int:pk>/editar/", ReservaUpdate.as_view(), name="update"),
    path("<int:pk>/eliminar/", ReservaDelete.as_view(), name="delete"),
]
