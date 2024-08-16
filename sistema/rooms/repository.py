from rooms.models import Room

class RoomRepository:
    @staticmethod
    def get_all_rooms():
        """Retorna todas as salas."""
        return Room.objects.all()

    @staticmethod
    def get_room_by_id(room_id):
        """Retorna uma sala pelo ID."""
        try:
            return Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return None

    @staticmethod
    def create_room(name):
        """Cria uma nova sala."""
        return Room.objects.create(name=name)

    @staticmethod
    def update_room(room_id, name):
        """Atualiza uma sala existente."""
        room = RoomRepository.get_room_by_id(room_id)
        if room:
            room.name = name
            room.save()
            return room
        return None

    @staticmethod
    def delete_room(room_id):
        """Deleta uma sala pelo ID."""
        room = RoomRepository.get_room_by_id(room_id)
        if room:
            room.delete()
            return True
        return False