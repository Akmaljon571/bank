from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import CreditModel
from .serializers import CreditSerializers


class CreditAllViews(ListAPIView):
    queryset = CreditModel.objects.all()
    serializer_class = CreditSerializers


class CreditOneViews(RetrieveAPIView):
    queryset = CreditModel.objects.all()
    serializer_class = CreditSerializers
