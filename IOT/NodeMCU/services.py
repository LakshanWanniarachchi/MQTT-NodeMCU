import paho.mqtt.client as mqtt
from .models import SensorData
# MQTT Configuration
MQTT_BROKER = "af506f8e7c3544458df791a91afc05c0.s1.eu.hivemq.cloud"
MQTT_PORT = 8883
MQTT_USERNAME = "lakshan"
MQTT_PASSWORD = "P2hndb@12345"
SUBSCRIBE_TOPIC = "outTopic"
PUBLISH_TOPIC = "inTopic"

# Global MQTT client instance
client = mqtt.Client()


# Callback when a message is received
def on_message(client, userdata, msg):  # Import here to avoid circular dependency
    message = msg.payload.decode()
    topic = msg.topic
    print(f"Received message: '{message}' on topic '{topic}'")

    # Save to database
    SensorData.objects.create(topic=topic, message=message)


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
