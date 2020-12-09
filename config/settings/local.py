from .base import *

# cors headers
INSTALLED_APPS += ['corsheaders',]
MIDDLEWARE += ['corsheaders.middleware.CorsMiddleware',]
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DJANGO_DB_NAME'),
        'USER': os.environ.get('DJANGO_DB_USERNAME'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD'),
        'HOST': os.environ.get('DJANGO_DB_HOST'),
        'PORT': os.environ.get('DJANGO_DB_PORT'),
    },
    'sub_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('SUB_DB_NAME'),
        'USER': os.environ.get('SUB_DB_USERNAME'),
        'PASSWORD': os.environ.get('SUB_DB_PASSWORD'),
        'HOST': os.environ.get('SUB_DB_HOST'),
        'PORT': '5432',
    }
}

DATABASE_ROUTERS = ['core.routers.MultiDBRouter']

# logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}