from django.urls import path
from kitaplar.api import views as api_view

urlpatterns = [
    # path('kitaplar/<int:pk>', api_view.KitaplarDetailsAPIView.as_view(), name='kitap-detail'),
    path('kitaplar/', api_view.KitaplarListCreateAPIView.as_view(), name='kitap-list')
]
