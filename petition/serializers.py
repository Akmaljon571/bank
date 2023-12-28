from rest_framework.serializers import ModelSerializer

from .models import PetitionModel


class PetitionsSerializers(ModelSerializer):
    class Meta:
        model = PetitionModel
        fields = "__all__"
        

class PetitionsImageSerializers(ModelSerializer):
    class Meta:
        model = PetitionModel
        fields = ('image',)
