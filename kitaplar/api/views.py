from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.mixins import *
from rest_framework.views import APIView
from kitaplar.models import Kitap, Yorum
from kitaplar.api.serializers import KitapSerializer, YorumSerializer
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

class KitaplarListCreateAPIView(ListCreateAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer

class KitaplarDetailsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer

class YorumCreateAPIView(CreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer

    def perform_create(self, serializer):
        kitap_pk = self.kwargs.get('kitap_pk')
        kitap = get_object_or_404(Kitap, pk=kitap_pk)
        serializer.save(kitap=kitap)

class YorumDetailsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer

# class KitaplarListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Kitap.objects.all()
#     serializer_class = KitapSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)