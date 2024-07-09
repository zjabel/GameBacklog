from .models import User


def create_user(username, birth_date, email):
    return User.objects.create(username=username, birth_date=birth_date, email=email)


def get_user_by(id):
    return User.objects.get(id=id)


def delete_user_by(id):
    user = User.objects.get(id=id)
    user.delete()


def update_user_by(id,  email):
    user = User.objects.get(id=id)
    user.email = email
    user.save()