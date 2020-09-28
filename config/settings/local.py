from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DJANGO_DB_NAME', 'sampledb'),
        'USER': os.environ.get('DJANGO_DB_USERNAME', 'sampleuser'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', 'samplesecret'),

        # if not use docker container as django server
        # 'HOST': os.environ.get('DJANGO_DB_HOST', 'localhost'),

        'HOST': os.environ.get('DJANGO_DB_HOST', 'db'),

        'PORT': os.environ.get('DJANGO_DB_PORT', '5432'),
    }
}

STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')