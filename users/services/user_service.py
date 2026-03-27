from users.repositories.user_repository import UserRepository

class UserService:

    @staticmethod
    def register_user(username, email, password):
        
        # Check if email already exists
        existing_user = UserRepository.get_user_by_email(email)
        if existing_user:
            return {"error": "Email already exists"}

        # Create user
        user = UserRepository.create_user(username, email, password)

        return {"success": "User registered successfully", "user": user}