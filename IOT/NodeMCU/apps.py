from django.apps import AppConfig
from threading import Thread
from .services import start_mqtt_client


class NodeMCUConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'NodeMCU'

    def ready(self):
        # Start the MQTT client in a separate thread
        mqtt_thread = Thread(target=start_mqtt_client)
        mqtt_thread.daemon = True  # Ensure thread stops with the app
        mqtt_thread.start()
