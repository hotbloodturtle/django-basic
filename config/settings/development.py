from .base import *

# cors headers
INSTALLED_APPS += ['corsheaders',]
MIDDLEWARE += ['corsheaders.middleware.CorsMiddleware',]
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DJANGO_DB_NAME', 'sampledb'),
        'USER': os.environ.get('DJANGO_DB_USERNAME', 'sampleuser'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', 'samplesecret'),
        'HOST': os.environ.get('DJANGO_DB_HOST', 'db'),
        'PORT': os.environ.get('DJANGO_DB_PORT', '5432'),
    }
}

STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')
