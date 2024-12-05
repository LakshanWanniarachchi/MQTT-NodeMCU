from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import publish_message
from .models import SensorData


@csrf_exempt
def send_message_view(request):
    """
    Django view to publish a message to the MQTT topic.
    """
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            publish_message(message)
            return JsonResponse({'status': 'success', 'message': f"Message '{message}' sent."})
        return JsonResponse({'status': 'error', 'message': 'No message provided.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def get_sensor_data(request):
    """
    API endpoint to fetch the sensor data.
    """
    data = SensorData.objects.all().order_by(
        '-timestamp').values('topic', 'message', 'timestamp')
    return JsonResponse({'data': list(data)}, safe=False)
