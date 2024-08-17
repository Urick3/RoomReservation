from django.urls import path
from .views import *

# Create your views here.

urlpatterns = [
    path("listar/", RoomListView.as_view(), name="all_rooms"),
    path("criar/", RoomCreateView.as_view(), name="create_rooms"),
    path("editar/<int:rooms_id>/", RoomUpdateView.as_view(), name="edit_rooms"),
    path("deletar/<int:rooms_id>/", RoomDeleteView.as_view(), name="delete_rooms"),

]