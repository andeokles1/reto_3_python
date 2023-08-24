from ..models import Account
from ..models import User
from ..models import Card
import datetime


class AccountController:

    @staticmethod
    def create_account(user: User, accountNumber: str, balance: float, open_date: datetime.datetime,
                       limit: float):
        account = Account.objects.create(user_id=user, account_number=accountNumber, balance=balance,
                                         open_date=open_date, limit=limit)
        account.save()
        return account

    # read
    @staticmethod
    def get_account_list(query: str):
        return Account.objects.filter(id__contains=query)

    @staticmethod
    def get_account_by_id(account_id: int):
        return Account.objects.get(id=account_id)

    @staticmethod
    def get_account_by_number(account_number: int):
        return Account.objects.get(account_number=account_number)

    @staticmethod
    def get_account_by_user(user: User):
        print(f'user id {user.id}')
        try:
            return Account.objects.get(user_id=user.id)
        except Account.DoesNotExist:
            return None

    @staticmethod
    def update_balance(account: Account, amount: float) -> bool:
        balance = account.balance + amount
        limit = account.limit
        if balance >= -limit:
            account.balance += amount
            account.save()
        else:
            raise RuntimeError('Not enough credit')

    @staticmethod
    def delete_account(id: int):
        account = AccountController.get_account_by_id(account_id=id)
        try:
            card = Card.objects.get(account_number=account.account_number)
        except:
            card = None

        if card is None:
            account.delete()
        else:
            account.delete()
            card.delete()
