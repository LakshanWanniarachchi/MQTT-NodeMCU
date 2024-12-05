from django.db import models


class SensorData(models.Model):
    topic = models.CharField(max_length=255)  # MQTT topic
    message = models.TextField()             # Received message
    # Automatically record when data was received
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic}: {self.message} @ {self.timestamp}"
