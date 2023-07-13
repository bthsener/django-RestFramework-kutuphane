from rest_framework import serializers
from django.db import models
from rest_framework.generics import get_object_or_404


def get_object(self, pk):
    model_instance = get_object_or_404(models, pk=pk)
    return model_instance


def SerializationUtilImp(serializers, request, models, pk=None):
    if request.method=='GET':
        model = get_object(pk)
        serializer_model = serializers(model)
        return serializer_model.data