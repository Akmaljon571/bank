from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import PetitionsSerializers, PetitionsImageSerializers
from .models import PetitionModel


class CreateView(APIView):
    parser_classes = (MultiPartParser,)
    serializer_class = PetitionsImageSerializers

    def post(self, request, *args, **kwargs):
        serializer = PetitionsImageSerializers(data=request.data)

        if serializer.is_valid():
            a = serializer.save()
            return Response({'image': serializer.data['image'], 'id': a.id}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateView(UpdateAPIView):
    queryset = PetitionModel.objects.all()
    serializer_class = PetitionsSerializers
