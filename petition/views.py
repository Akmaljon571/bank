from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser

from .serializers import PetitionsSerializers
from .models import PetitionModel


class CreateView(CreateAPIView):
    parser_classes = (MultiPartParser,)
    queryset = PetitionModel.objects.all()
    serializer_class = PetitionsSerializers
