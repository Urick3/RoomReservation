from reservations.reservation_repository import HourRepository
from reservations.reservation_repository  import ReservationRepository
from reservations.reservation_repository  import ReservationApprovalRepository
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