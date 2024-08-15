from rooms.room_repository import RoomRepository

class RoomService:
    @staticmethod
    def list_all_rooms():
        """Lista todas as salas disponíveis."""
        return RoomRepository.get_all_rooms()

    @staticmethod
    def get_room_details(room_id):
        """Obtém os detalhes de uma sala específica."""
        return RoomRepository.get_room_by_id(room_id)

    @staticmethod
    def create_new_room(name):
        """Cria uma nova sala."""
        return RoomRepository.create_room(name)

    @staticmethod
    def update_existing_room(room_id, name):
        """Atualiza uma sala existente."""
        return RoomRepository.update_room(room_id, name)

    @staticmethod
    def delete_room(room_id):
        """Remove uma sala do sistema."""
        return RoomRepository.delete_room(room_id)