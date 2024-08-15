from django.shortcuts import redirect, render,get_object_or_404
from rooms.models import  *
from rooms.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def read_rooms():
    return

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

    