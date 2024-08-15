from users.user_repository import UserRepository
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class UserService:
    @staticmethod
    @staticmethod
    def list_all_users(page=1, per_page=10):
        """
        Lista todos os usuários com paginação.

        :param page: Número da página atual.
        :param per_page: Quantidade de itens por página.
        :return: Página atual com os usuários e informações de paginação.
        """
        all_users = UserRepository.get_all_users()
        paginator = Paginator(all_users, per_page)

        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)

        return users

    @staticmethod
    def get_user_details(user_id):
        """Obtém os detalhes de um usuário específico."""
        return UserRepository.get_user_by_id(user_id)

    @staticmethod
    def create_new_user(**kwargs):
        """Cria um novo usuário."""
        return UserRepository.create_user(**kwargs)

    @staticmethod
    def update_existing_user(user_id, **kwargs):
        """Atualiza um usuário existente."""
        return UserRepository.update_user(user_id, **kwargs)

    @staticmethod
    def delete_user(user_id):
        """Remove um usuário do sistema."""
        return UserRepository.delete_user(user_id)