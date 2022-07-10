import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-j=4$9&z_m_3efti7w)9h^3yg1b55!4(+al857snlsx3#qx)&2y'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kino_site',
        'USER': 'tixon',
        'PASSWORD': 'gft654gfhgf',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'movies/static/movies'),
]