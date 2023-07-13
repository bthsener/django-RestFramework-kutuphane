from rest_framework import status
from rest_framework.views import APIView
from kitaplar.models import Kitap, Yorum
from kitaplar.api.serializers import KitapSerializer, YorumSerializer
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

