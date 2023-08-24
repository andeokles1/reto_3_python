from ..models import User
from ..serializers import UserSerializer
from ..controllers.account_controller import AccountController
from django.db.models import Q

class UserController:

    @staticmethod
    def create_user(name: str, age: int) -> User:
        return User.objects.create(name=name, age=age)


    @staticmethod
    def get_user_list(query:str):
        users = User.objects.filter(Q(id__contains=query) | Q(name__contains=query) | Q(age__contains=query))
        serializer = UserSerializer(users, many=True)
        return serializer.data

    @staticmethod
    def get_object(name):
        try:
            return User.objects.get(name=name)
        except User.DoesNotExist:
            raise RuntimeError('User does not exist')
    @staticmethod
    def get_user_by_name(name: str):
        return UserController.get_object(name=name)

    @staticmethod
    def get_user_by_id(id: int):
        return User.objects.get(id=id)


    @staticmethod
    def update_user(username_toupdate: str, name: str, age:int):
        user = UserController.get_object(name=username_toupdate)
        user.name = name
        user.age = age
        user.save()
        return user

    @staticmethod
    def delete_user(name: str):
        user = UserController.get_object(name=name)
        print(f'user id {user.id}')
        try:
            account = AccountController.get_account_by_user(user=user)
        except:
            account = None

        if account is None:
            user.delete()
        else:
            AccountController.delete_account(account)
            user.delete()



