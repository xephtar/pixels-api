from django.utils import timezone
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pixelsapi.settings')
django.setup()

try:
    from canvas.models import Check
    expired_checks = Check.objects.filter(end_time__lt=timezone.now()).delete()
    print("Expired checks are deleted!")
except Exception as e:
    print(e)
    print("Expired checks could not be deleted!")
