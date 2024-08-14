from users.models import User

class UserRepository:
    
    @staticmethod
    def get_user_by_id(user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    @staticmethod
    def delete_user(user_id):
        User.objects.filter(pk=user_id).delete()

    @staticmethod
    def create_user(data):
        return User.objects.create(**data)

    @staticmethod
    def update_user(user, data):
        for key, value in data.items():
            setattr(user, key, value)
        user.save()
        return user
    
    @staticmethod
    def get_all_users():
        return User.objects.all()
    