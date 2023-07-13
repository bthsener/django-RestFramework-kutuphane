from django.urls import path
from kitaplar.api import views as api_view

urlpatterns = [
    path('kitaplar/', api_view.KitaplarListCreateAPIView.as_view(), name='kitap-list'),
    path('kitaplar/<int:pk>', api_view.KitaplarDetailsAPIView.as_view(), name='kitap-detaylari'),
    path('kitaplar/<int:kitap_pk>/yorum', api_view.YorumCreateAPIView.as_view(), name='yorum-yap'),
    path('yorumlar/<int:pk>', api_view.YorumDetailsAPIView.as_view(), name='yorum-detaylari'),
]
