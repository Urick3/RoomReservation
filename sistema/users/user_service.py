from users.user_repository import UserRepository

class UserService:
    @staticmethod
    def list_all_users():
        """Lista todos os usuários do sistema."""
        return UserRepository.get_all_users()

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