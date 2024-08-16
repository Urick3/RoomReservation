from django.urls import path
from .views import *

# Create your views here.

urlpatterns = [
    path("salas/", room_list_view, name="all_rooms"),
    path("salas/criar/", create_rooms, name="Create"),
    path("salas/editar/<int:rooms_id>/", edit_rooms, name="Edit"),
    path("salas/deletar/<int:rooms_id>/", delete_rooms, name="Delete"),

]