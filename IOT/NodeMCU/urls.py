from django.urls import path
from .views import send_message_view, get_sensor_data

urlpatterns = [
    path('send-message', send_message_view),
    path('get-sensor-data', get_sensor_data),
]
