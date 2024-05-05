from django.urls import path
from .views import *

urlpatterns = [
    path('', MainList.as_view(), name='index'),
    path('final/', final, name='final'),
    path('register/', register, name='register'),  # URL-маршрут для обработки регистрации
]
