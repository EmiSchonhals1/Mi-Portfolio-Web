import os
from django.core.asgi import get_asgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')

application = get_asgi_application()
application = WhiteNoise(application)