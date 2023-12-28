from rest_framework.serializers import ModelSerializer

from .models import CreditModel


class CreditSerializers(ModelSerializer):
    class Meta:
        model = CreditModel
        fields = '__all__'
