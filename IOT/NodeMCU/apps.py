from django.apps import AppConfig
from threading import Thread


class NodeMCUConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'NodeMCU'

    def ready(self):
        # Import here to avoid premature model loading
        from .services import start_mqtt_client
        mqtt_thread = Thread(target=start_mqtt_client)
        mqtt_thread.daemon = True  # Ensure thread stops with the app
        mqtt_thread.start()
