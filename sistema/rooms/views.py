from django.shortcuts import redirect, render,get_object_or_404
from rooms.models import  *
from rooms.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rooms.service import RoomService

def room_list_view(request):
    page = request.GET.get('page', 1)
    per_page = 10  # ou você pode tornar isso dinâmico também
    
    rooms = RoomService.list_all_rooms(page=page, per_page=per_page)
    
    return render(request, 'rooms/classrooms.html', {'rooms': rooms})



def create_rooms():
    return

def edit_rooms():
    return

@login_required
def delete_rooms(request, rooms_id):
    room = get_object_or_404(Room, id=rooms_id)
    if request.method == 'POST':
        room.delete()
        messages.success(request, 'Sala deletada com sucesso!')
        return redirect('read')
    return render(request, 'rooms/delete.html')

    