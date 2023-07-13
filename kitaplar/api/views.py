from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.mixins import *
from rest_framework.views import APIView
from kitaplar.models import Kitap, Yorum
from kitaplar.api import permissions
from kitaplar.api.serializers import KitapSerializer, YorumSerializer
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

class KitaplarListCreateAPIView(ListCreateAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer
    permission_classes = [permissions.isAdminorReadOnly]

class KitaplarDetailsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer
    permission_classes = [permissions.isAdminorReadOnly]

class YorumCreateAPIView(CreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [permissions.isUserorReadOnly]

    def perform_create(self, serializer):
        kitap_pk = self.kwargs.get('kitap_pk')
        kitap = get_object_or_404(Kitap, pk=kitap_pk)
        user = self.request.user
        yorumlar = Yorum.objects.filter(kitap=kitap, yorum_sahibi=user)
        if yorumlar.exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)# raise "yalnizca bir yorum yapabilirsiniz."
        serializer.save(kitap=kitap, yorum_sahibi=user)

class YorumDetailsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [permissions.isYorumSahibiOrReadOnly]

# class KitaplarListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Kitap.objects.all()
#     serializer_class = KitapSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)