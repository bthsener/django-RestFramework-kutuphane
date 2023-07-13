from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import *
from rest_framework.views import APIView
from kitaplar.models import Kitap, Yorum
from kitaplar.api.serializers import KitapSerializer, YorumSerializer
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

class KitaplarListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)