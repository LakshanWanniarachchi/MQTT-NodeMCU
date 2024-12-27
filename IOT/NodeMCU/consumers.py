from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .services import publish_message


class SensorDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Add the WebSocket to the sensor data group
        await self.channel_layer.group_add("sensor_data_group", self.channel_name)
        await self.accept()
        print(f"WebSocket connected: {self.scope['client']}")

    async def disconnect(self, close_code):
        # Remove the WebSocket from the sensor data group
        await self.channel_layer.group_discard("sensor_data_group", self.channel_name)
        print(
            f"WebSocket disconnected: {self.scope['client']} with close code {close_code}")

    async def receive(self, text_data):
        try:
            # Parse the text_data string into a dictionary
            data = json.loads(text_data)
            print(f"Message received: {data}")

            # Access the 'inputValue' key from the parsed dictionary
            input_value = data.get('inputValue')

            # Ensure input_value is valid before publishing the message
            if input_value is not None:
                publish_message(input_value)

            # Optionally, respond back to the WebSocket client
            await self.send(text_data=json.dumps({"message": f"Server received: {input_value}"}))
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            await self.send(text_data=json.dumps({"error": "Invalid JSON format"}))

    async def send_sensor_data(self, event):
        # Send MQTT data to WebSocket clients
        message = event["message"]
        await self.send(text_data=json.dumps({
            "topic": message["topic"],
            "data": message["data"]
        }))
