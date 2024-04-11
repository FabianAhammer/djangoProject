from django.http import JsonResponse
from django.core import serializers

from .models import Message


# Create your views here.


def messages(request):
    if request.method == "GET":
        return JsonResponse(serializers.serialize("json", Message.objects.all()), safe=False)
