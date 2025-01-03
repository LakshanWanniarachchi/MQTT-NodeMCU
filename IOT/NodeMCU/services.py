# mqtt_client.py

import json
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import paho.mqtt.client as mqtt

# MQTT Configuration
MQTT_BROKER = "af506f8e7c3544458df791a91afc05c0.s1.eu.hivemq.cloud"
MQTT_PORT = 8883
MQTT_USERNAME = "lakshan"
MQTT_PASSWORD = "P2hndb@12345"
SUBSCRIBE_TOPIC = "outTopic"
PUBLISH_TOPIC = "inTopic"

# Global MQTT client instance
client = mqtt.Client()


def on_message(client, userdata, msg):
    message = msg.payload.decode()
    topic = msg.topic
    print(f"Received message: '{message}' on topic '{topic}'")

    # Save to database
    from .models import SensorData

    SensorData.objects.create(topic=topic, message=message)

    # Broadcast the message to WebSocket clients
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "sensor_data_group",  # Group name
        {
            "type": "send_sensor_data",  # Event name
            "message": {"topic": topic, "data": message},  # Payload
        },
    )


def start_mqtt_client():
    """
    Starts the MQTT client for subscribing and listening to messages.
    """
    try:
        client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        client.tls_set()  # Enable TLS
        client.on_message = on_message  # Assign the message callback
        client.connect(MQTT_BROKER, MQTT_PORT, 60)  # Connect to the broker
        client.subscribe(SUBSCRIBE_TOPIC)  # Subscribe to the topic
        print(f"Subscribed to topic '{SUBSCRIBE_TOPIC}'.")
        client.loop_start()  # Start the client loop in a separate thread
    except Exception as e:
        print(f"Error starting MQTT client: {e}")


def publish_message(message):
    """
    Publishes a message to the specified topic.
    :param message: The message string to send to the subscriber.
    """
    try:
        client.publish(PUBLISH_TOPIC, message)
        print(f"Message '{message}' sent to topic '{PUBLISH_TOPIC}'.")
    except Exception as e:
        print(f"Error publishing message: {e}")
