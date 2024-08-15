from reservations.models import Hour
from reservations.models import Reservation
from reservations.models import ReservationApproval

class ReservationApprovalRepository:
    @staticmethod
    def get_all_approvals():
        """Retorna todas as aprovações de reservas."""
        return ReservationApproval.objects.all()

    @staticmethod
    def get_approval_by_id(approval_id):
        """Retorna uma aprovação de reserva pelo ID."""
        try:
            return ReservationApproval.objects.get(id=approval_id)
        except ReservationApproval.DoesNotExist:
            return None

    @staticmethod
    def create_approval(reservation, manager):
        """Cria uma nova aprovação de reserva."""
        return ReservationApproval.objects.create(
            reservation=reservation,
            manager=manager
        )
    

    
class ReservationRepository:
    @staticmethod
    def get_all_reservations():
        """Retorna todas as reservas."""
        return Reservation.objects.all()

    @staticmethod
    def get_reservation_by_id(reservation_id):
        """Retorna uma reserva pelo ID."""
        try:
            return Reservation.objects.get(id=reservation_id)
        except Reservation.DoesNotExist:
            return None

    @staticmethod
    def create_reservation(room, teacher, hour, date, status='pending'):
        """Cria uma nova reserva."""
        return Reservation.objects.create(
            room=room,
            teacher=teacher,
            hour=hour,
            date=date,
            status=status
        )

    @staticmethod
    def update_reservation(reservation_id, **kwargs):
        """Atualiza uma reserva existente."""
        reservation = ReservationRepository.get_reservation_by_id(reservation_id)
        if reservation:
            for key, value in kwargs.items():
                setattr(reservation, key, value)
            reservation.save()
            return reservation
        return None

    @staticmethod
    def delete_reservation(reservation_id):
        """Deleta uma reserva pelo ID."""
        reservation = ReservationRepository.get_reservation_by_id(reservation_id)
        if reservation:
            reservation.delete()
            return True
        return False
    
    @staticmethod
    def get_reservations_by_date_and_status(date, status):
        return Reservation.objects.filter(date=date, status=status)
    
    @staticmethod
    def get_reservations_by_room_date_and_status(room, date, status):
        """
        Retorna reservas com um determinado status para uma sala e data específicos.

        :param room: Sala para filtrar as reservas.
        :param date: Data para filtrar as reservas.
        :param status: Status das reservas (e.g. 'approved').
        :return: Queryset de reservas filtradas.
        """
        return Reservation.objects.filter(room=room, date=date, status=status)



class HourRepository:
    @staticmethod
    def get_all_hours():
        """Retorna todos os horários."""
        return Hour.objects.all()

    @staticmethod
    def get_hour_by_id(hour_id):
        """Retorna um horário pelo ID."""
        try:
            return Hour.objects.get(id=hour_id)
        except Hour.DoesNotExist:
            return None

    @staticmethod
    def create_hour(range_hour):
        """Cria um novo horário."""
        return Hour.objects.create(range_hour=range_hour)

    @staticmethod
    def update_hour(hour_id, range_hour):
        """Atualiza um horário existente."""
        hour = HourRepository.get_hour_by_id(hour_id)
        if hour:
            hour.range_hour = range_hour
            hour.save()
            return hour
        return None

    @staticmethod
    def delete_hour(hour_id):
        """Deleta um horário pelo ID."""
        hour = HourRepository.get_hour_by_id(hour_id)
        if hour:
            hour.delete()
            return True
        return False
    
    @staticmethod
    def filter_hours_excluding_ids(hours, excluded_ids):
        """
        Filtra horas removendo aquelas cujos IDs estão na lista de excluídos.

        :param hours: Queryset de horas para filtrar.
        :param excluded_ids: Lista de IDs a serem excluídos.
        :return: Queryset de horas filtradas.
        """
        return hours.exclude(id__in=excluded_ids)