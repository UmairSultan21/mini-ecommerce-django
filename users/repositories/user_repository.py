from users.models import CustomUser

class UserRepository:

    @staticmethod
    def create_user(username, email, password):
        return CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password
        )

    @staticmethod
    def get_user_by_email(email):
        return CustomUser.objects.filter(email=email).first()