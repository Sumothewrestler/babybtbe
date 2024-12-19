from rest_framework import serializers
from .models import Business, Type, Ledger, Head, Mode, Transaction

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = '__all__'

class HeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Head
        fields = '__all__'

class ModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mode
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['business'] = instance.business.name
        representation['type'] = instance.type.name
        representation['ledger'] = instance.ledger.name
        representation['head'] = instance.head.name
        representation['mode'] = instance.mode.name
        return representation
    
    