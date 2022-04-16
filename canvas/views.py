import json
from django.http import HttpResponse
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from canvas.models import Check, CanvasData
from PIL import Image, ImageDraw
from rest_framework import serializers


class CanvasSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanvasData
        fields = ['id', 'data', 'created_at']


def index(request):
    return HttpResponse(status=200)


def getImage(request):
    size = (1024, 512)  # size of the image to create
    im = Image.new('RGB', size, color="white")  # create the image
    draw = ImageDraw.Draw(im)  # create a drawing object that is

    history = CanvasData.objects.order_by('created_at').all()
    serializer = CanvasSerializer(history, many=True)

    for data in serializer.data:
        json_data = json.loads(data['data'])
        x = json_data['x']
        y = json_data['y']
        color = json_data['color']
        draw.rectangle([(x, y), (x + 3, y + 3)], fill=color)
    del draw  # I'm done drawing so I don't need this anymore
    # We need an HttpResponse object with the correct mimetype
    response = HttpResponse(content_type="image/png")
    im.save(response, 'PNG')
    return response  # and we're done!


class DrawView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            last_check = Check.objects.get(user_id=request.user.id)
        except Check.DoesNotExist:
            last_check = None

        if not last_check:
            return Response(data={"canDraw": True}, status=200)

        if last_check:
            time = last_check.end_time < timezone.now()

            if time:
                return Response(data={"canDraw": True}, status=200)

        now = timezone.now()
        remaining = (last_check.end_time - now).seconds
        return Response(data={"canDraw": False, "exp": remaining}, status=200)

    def post(self, request):
        try:
            last_check = Check.objects.get(user_id=request.user.id)
        except Check.DoesNotExist:
            last_check = Check.objects.create(user_id=request.user.id, end_time=timezone.now() + timezone.timedelta(minutes=3))
            last_check.save()

        # First draw
        if not last_check:
            return Response(data={"canDraw": True, "exp": 180}, status=200)

        time = last_check.end_time < timezone.now()

        if time:
            last_check.end_time = timezone.now() + timezone.timedelta(minutes=3)
            last_check.save()
            return Response(data={"canDraw": True, "exp": (last_check.end_time - timezone.now()).seconds}, status=200)

        remaining = (last_check.end_time - timezone.now()).seconds
        return Response(data={"canDraw": False, "exp": remaining}, status=200)
