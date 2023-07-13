from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Kitap(models.Model):
    isim = models.CharField(max_length=120)
    yazar = models.CharField(max_length=120)
    aciklama = models.TextField()

    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True)
    yayin_tarihi = models.DateTimeField()


class Yorum(models.Model):
    kitap = models.ForeignKey(Kitap, on_delete=models.CASCADE, related_name='yorumlar')

    yorum_sahibi = models.CharField(max_length=120)
    yorum = models.TextField()

    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True)

    degerlendirme = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )