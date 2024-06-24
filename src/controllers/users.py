from src.models.user import User

def get_users():
    return User.get_all()

def create_user(data):
    return User.create(data)