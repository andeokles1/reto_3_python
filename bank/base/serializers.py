from rest_framework.serializers import ModelSerializer
from .models import Payment, User, Account, Charge, Card


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class AccountSerializer(ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'


class CardSerializer(ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class ChargeSerializer(ModelSerializer):

    class Meta:
        model = Charge
        fields = '__all__'
