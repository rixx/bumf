"""
Django settings for bumf.
"""
import os
import string

from django.utils.crypto import get_random_string

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


secret_file = os.path.join(BASE_DIR, '.secret')
if os.path.exists(secret_file):
    with open(secret_file, 'r') as secret_stream:
        SECRET_KEY = secret_stream.read().strip()
else:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    SECRET_KEY = get_random_string(length=50, allowed_chars=alphabet)

    with open(secret_file, 'w') as secret_stream:
        os.chmod(secret_file, 0o600)
        os.chown(secret_file, os.getuid(), os.getgid())
        secret_stream.write(SECRET_KEY)

DEBUG = True
ALLOWED_HOSTS = []


BASE_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

EXTERNAL_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
]

LOCAL_APPS = [
    'bumf.api',
    'bumf.core',
]

INSTALLED_APPS = BASE_APPS + EXTERNAL_APPS + LOCAL_APPS

try:
    import django_extensions
    INSTALLED_APPS.append('django_extensions')
except ImportError:
    pass

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bumf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bumf.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_USER_MODEL = 'core.User'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'


#### App configuration
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'


#### Debug config

if DEBUG is True:
    INSTALLED_APPS.append('corsheaders')
    MIDDLEWARE.append('corsheaders.middleware.CorsMiddleware')
    CORS_ORIGIN_ALLOW_ALL = True

    INSTALLED_APPS.append('rest_framework_swagger')

    SWAGGER_SETTINGS = {
        'SECURITY_DEFINITIONS': {
            'api_key': {
                'type': 'apiKey',
                'in': 'header',
                'name': 'Authorization'
            }
        },
    }
