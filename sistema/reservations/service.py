from reservations.repository import HourRepository
from reservations.repository  import ReservationRepository
from reservations.repository  import ReservationApprovalRepository
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ReservationApprovalService:
    @staticmethod
    def list_all_approvals(page=1, per_page=10):
        """
        Lista todas as aprovações de reservas com paginação.

        :param page: Número da página atual.
        :param per_page: Quantidade de itens por página.
        :return: Página atual com as aprovações e informações de paginação.
        """
        all_approvals = ReservationApprovalRepository.get_all_approvals()
        paginator = Paginator(all_approvals, per_page)

        try:
            approvals = paginator.page(page)
        except PageNotAnInteger:
            approvals = paginator.page(1)
        except EmptyPage:
            approvals = paginator.page(paginator.num_pages)

        return approvals

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
    def list_all_reservations(page=1, per_page=10):
        """
        Lista todas as reservas com paginação.

        :param page: Número da página atual.
        :param per_page: Quantidade de itens por página.
        :return: Página atual com as reservas e informações de paginação.
        """
        all_reservations = ReservationRepository.get_all_reservations()
        paginator = Paginator(all_reservations, per_page)

        try:
            reservations = paginator.page(page)
        except PageNotAnInteger:
            # Se a página não for um inteiro, entrega a primeira página
            reservations = paginator.page(1)
        except EmptyPage:
            # Se a página estiver fora do intervalo (e.g. 9999), entrega a última página de resultados
            reservations = paginator.page(paginator.num_pages)

        return reservations

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
    
    @staticmethod
    def approve_reservation(reservation_id, manager):
        """
        Aprova uma reserva pendente. Atualiza o status da reserva e cria um registro de aprovação.

        :param reservation_id: ID da reserva a ser aprovada.
        :param manager: Instância do usuário gestor que está aprovando a reserva.
        :return: Reserva aprovada ou mensagem de erro.
        """
        try:
            reservation = ReservationRepository.get_reservation_by_id(reservation_id)

            if reservation.status != 'pending':
                return {"error": "Reserva não está em estado pendente."}

            # Atualiza o status da reserva para 'approved'
            updated_reservation = ReservationRepository.update_reservation(reservation_id, status='approved')

            # Cria um registro de aprovação
            ReservationApprovalService.create_new_approval(reservation=updated_reservation, manager=manager)

            return updated_reservation

        except ReservationApprovalService.DoesNotExist:
            return {"error": "Reserva não encontrada."}

    @staticmethod
    def list_pending_reservations_by_date(date):
        """
        Lista todas as reservas pendentes para uma data específica.

        :param date: Data para buscar as reservas pendentes.
        :return: Lista de reservas pendentes.
        """
        return ReservationRepository.get_reservations_by_date_and_status(date, 'pending')


    @staticmethod
    def list_available_hours_for_date(room, date):
        """
        Lista todas as horas disponíveis para uma sala em uma data específica.

        :param room: Sala para verificar a disponibilidade.
        :param date: Data para verificar a disponibilidade.
        :return: Lista de horas disponíveis.
        """
        # Passo 1: Obter todas as reservas aprovadas para a data e sala específica
        approved_reservations = ReservationRepository.get_reservations_by_room_date_and_status(room, date, 'approved')
        
        # Passo 2: Obter os IDs das horas que já estão reservadas
        occupied_hour_ids = approved_reservations.values_list('hour_id', flat=True)

        # Passo 3: Obter todas as horas disponíveis usando o HourService
        all_hours = HourService.get_all_hours()

        # Passo 4: Filtrar as horas disponíveis removendo as ocupadas
        available_hours = HourService.get_available_hours(all_hours, occupied_hour_ids)

        return available_hours



class HourService:
    @staticmethod
    def list_all_hours(page=1, per_page=10):
        """
        Lista todos os horários com paginação.

        :param page: Número da página atual.
        :param per_page: Quantidade de itens por página.
        :return: Página atual com os horários e informações de paginação.
        """
        all_hours = HourRepository.get_all_hours()
        paginator = Paginator(all_hours, per_page)

        try:
            hours = paginator.page(page)
        except PageNotAnInteger:
            hours = paginator.page(1)
        except EmptyPage:
            hours = paginator.page(paginator.num_pages)

        return hours

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
    

    @staticmethod
    def get_all_hours():
        """
        Retorna todas as horas disponíveis no sistema.
        """
        return HourRepository.get_all_hours()

    @staticmethod
    def get_available_hours(all_hours, occupied_hour_ids):
        """
        Filtra as horas disponíveis removendo as ocupadas.

        :param all_hours: Queryset de todas as horas.
        :param occupied_hour_ids: Lista de IDs de horas ocupadas.
        :return: Queryset de horas disponíveis.
        """
        return HourRepository.filter_hours_excluding_ids(all_hours, occupied_hour_ids)














"""
Formas de enviar o email:
from notifications.services import EmailService

# Exemplo de envio de um email de texto simples
EmailService.send_text_email(
    subject="Sua reserva foi confirmada",
    message="Sua reserva para a sala XYZ foi confirmada.",
    recipient_list=["usuario@example.com"]
)

# Exemplo de envio de um email com corpo HTML
EmailService.send_html_email(
    subject="Sua reserva foi confirmada",
    html_content="<h1>Reserva Confirmada</h1><p>Sua reserva para a sala XYZ foi confirmada.</p>",
    recipient_list=["usuario@example.com"]
)

# Exemplo de envio de um email com anexo e corpo HTML
EmailService.send_email_with_attachment(
    subject="Documento Importante",
    message="Veja o documento em anexo.",
    recipient_list=["usuario@example.com"],
    attachment_path="/caminho/para/anexo.pdf",
    html_message="<p>Veja o documento em anexo.</p>"
)


#exemplo de envio com template html
context = {
    'user': user,
    'room': room,
    'reservation_date': reservation_date,
    'time_slot': time_slot,
}

EmailService.send_html_email_with_template(
    subject="Confirmação de Reserva",
    template_name="emails/email_confirmacao_reserva.html",
    context=context,
    recipient_list=[user.email]
)
"""





"""
# Exemplo de uso em uma view ou API
def check_availability(request, room_id, date):
    room = Room.objects.get(id=room_id)
    available_hours = ReservationService.list_available_hours_for_date(room, date)

    return JsonResponse({
        'available_hours': list(available_hours.values('id', 'range_hour'))
    })
"""