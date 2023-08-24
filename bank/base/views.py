import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from .controllers.user_controller import UserController
from .controllers.account_controller import AccountController
from .controllers.card_controller import CardController
from .controllers.payment_controller import PaymentController
from .controllers.charge_controller import ChargeController
from .serializers import UserSerializer, AccountSerializer, CardSerializer, ChargeSerializer, PaymentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def endpoints(request):
    data = ['api/token/', 'api/token/refresh/', 'users/', 'users/username', 'accounts/', 'accounts/id', 'cards/',
            'cards/id', 'charges/', 'charges/id''payments/', 'payments/id']
    return Response(data)


@permission_classes([IsAuthenticated])
class UserList(APIView):

    def get(self, request):
        query = request.GET.get('query')
        print('Query: ', query)
        if query == None:
            query = ''

        user = UserController.get_user_list(query=query)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = UserController.create_user(name=request.data['name'], age=request.data['age'])
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class UserDetail(APIView):

    def get(self, request, username):
        user = UserController.get_user_by_name(name=username)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    def put(self, request, username):
        user = UserController.update_user(username_toupdate=username, name=request.data['name'],
                                          age=request.data['age'])
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    def delete(self, request, username):
        UserController.delete_user(name=username)
        return Response('User has been deleted')


@permission_classes([IsAuthenticated])
class AccountList(APIView):
    def get(self, request):
        query = request.GET.get('query')
        print('Query: ', query)
        if query == None:
            query = ''

        account = AccountController.get_account_list(query=query)
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = UserController.get_user_by_id(id=request.data['user_id'])
        account = AccountController.create_account(user=user,
                                                   accountNumber=request.data['account_number'],
                                                   balance=request.data['balance'],
                                                   open_date=datetime.datetime.now(),
                                                   limit=request.data['limit'])
        serializer = AccountSerializer(account, many=False)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class AccountDetail(APIView):

    def get(self, request, id):
        account = AccountController.get_account_by_id(account_id=id)
        serializer = AccountSerializer(account, many=False)
        return Response(serializer.data)

    def delete(self, request, id):
        AccountController.delete_account(id=id)
        return Response('Account was deleted')


@permission_classes([IsAuthenticated])
class CardList(APIView):
    def get(self, request):
        query = request.GET.get('query')
        print('Query: ', query)
        if query == None:
            query = ''

        card = CardController.get_cards_list(query=query)
        serializer = CardSerializer(card, many=True)
        return Response(serializer.data)

    def post(self, request):
        account = AccountController.get_account_by_id(request.data['account_number'])
        card = CardController.create_card(account=account, name=request.data['name'], cvv=request.data['cvv'])
        serializer = CardSerializer(card, many=False)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class CardDetail(APIView):

    def get(self, request, id):
        card = CardController.get_card_by_id(id=id)
        serializer = CardSerializer(card, many=False)
        return Response(serializer.data)

    def put(self, request, id):
        card = CardController.update_cvv(card_id=id, cvv=request.data['cvv'])
        serializer = CardSerializer(card, many=False)
        return Response(serializer.data)

    def delete(self, request, id):
        print(f'id for card {id}')
        CardController.delete_card(id=id)
        return Response('Card was deleted')


@permission_classes([IsAuthenticated])
class PaymentList(APIView):
    def get(self, request):
        query = request.GET.get('query')
        print('Query: ', query)
        if query == None:
            query = ''

        payments = PaymentController.get_payment_list(query=query)
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request):
        card = CardController.get_card_by_id(request.data['card_id'])
        payment = PaymentController.make_a_payment(card=card, date_time=datetime.datetime.now(),
                                                   amount=request.data['amount'])
        serializer = PaymentSerializer(payment, many=False)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class PaymentDetail(APIView):

    def get(self, request, id):
        user = PaymentController.get_payment_id(id=id)
        serializer = PaymentSerializer(user, many=False)
        return Response(serializer.data)

    def delete(self, request, id):
        PaymentController.delete_payment(id=id)
        return Response('Payment was deleted')


@permission_classes([IsAuthenticated])
class ChargeList(APIView):
    def get(self, request):
        query = request.GET.get('query')
        print('Query: ', query)
        if query == None:
            query = ''

        charges = ChargeController.get_charges_list(query=query)
        serializer = ChargeSerializer(charges, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(f'card id gting from petitionet {request.data["card_id"]}')
        card = CardController.get_card_by_id(request.data['card_id'])
        print(f'card getting from petition {card.id}')
        print(f'card account id getting from petition {card.account_number}')
        charge = ChargeController.make_a_charge(card=card, date_time=datetime.datetime.now(),
                                                amount=request.data['amount'])
        serializer = ChargeSerializer(charge, many=False)
        return Response(serializer.data)

    # Create your views here.


@permission_classes([IsAuthenticated])
class ChargeDetail(APIView):

    def get(self, request, payment_id):
        charge = ChargeController.get_charge_id(id=payment_id)
        serializer = ChargeSerializer(charge, many=False)
        return Response(serializer.data)

    def delete(self, request, payment_id):
        ChargeController.delete_charge(id=payment_id)
        return Response('Payment was deleted')
