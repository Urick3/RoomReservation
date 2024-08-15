from reservations.reservation_repository import HourRepository
from reservations.reservation_repository  import ReservationRepository
from reservations.reservation_repository  import ReservationApprovalRepository

class ReservationApprovalService:
    @staticmethod
    def list_all_approvals():
        """Lista todas as aprovações de reservas."""
        return ReservationApprovalRepository.get_all_approvals()

    @staticmethod
    def get_approval_details(approval_id):
        """Obtém os detalhes de uma aprovação específica."""
        return ReservationApprovalRepository.get_approval_by_id(approval_id)

    @staticmethod
    def create_new_approval(reservation, manager):
        """Cria uma nova aprovação de reserva."""
        return ReservationApprovalRepository.create_approval(reservation, manager)
    




class ReservationService:
    @staticmethod
    def list_all_reservations():
        """Lista todas as reservas."""
        return ReservationRepository.get_all_reservations()

    @staticmethod
    def get_reservation_details(reservation_id):
        """Obtém os detalhes de uma reserva específica."""
        return ReservationRepository.get_reservation_by_id(reservation_id)

    @staticmethod
    def create_new_reservation(room, teacher, hour, date, status='pending'):
        """Cria uma nova reserva."""
        return ReservationRepository.create_reservation(room, teacher, hour, date, status)

    @staticmethod
    def update_existing_reservation(reservation_id, **kwargs):
        """Atualiza uma reserva existente."""
        return ReservationRepository.update_reservation(reservation_id, **kwargs)

    @staticmethod
    def delete_reservation(reservation_id):
        """Remove uma reserva do sistema."""
        return ReservationRepository.delete_reservation(reservation_id)
    



class HourService:
    @staticmethod
    def list_all_hours():
        """Lista todos os horários disponíveis."""
        return HourRepository.get_all_hours()

    @staticmethod
    def get_hour_details(hour_id):
        """Obtém os detalhes de um horário específico."""
        return HourRepository.get_hour_by_id(hour_id)

    @staticmethod
    def create_new_hour(range_hour):
        """Cria um novo horário."""
        return HourRepository.create_hour(range_hour)

    @staticmethod
    def update_existing_hour(hour_id, range_hour):
        """Atualiza um horário existente."""
        return HourRepository.update_hour(hour_id, range_hour)

    @staticmethod
    def delete_hour(hour_id):
        """Remove um horário do sistema."""
        return HourRepository.delete_hour(hour_id)