from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:user_pk>', views.detail, name='detail'),
]
