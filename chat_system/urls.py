from django.urls import path
from . import views

urlpatterns = [
    path('', views.messages, name='messages'),
    path('<int:product_id>/<int:user_id>',
         views.send_message, name='message'),
]
