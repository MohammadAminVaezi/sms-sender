from django.urls import path
from .views import send_text

urlpatterns = [
    path('send/', send_text, name='send-text'),
]
