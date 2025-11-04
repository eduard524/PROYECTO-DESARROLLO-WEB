from pathlib import Path


# RUTAS BASE

BASE_DIR = Path(__file__).resolve().parent.parent


# SEGURIDAD 

SECRET_KEY = 'django-insecure-h94erl+@cjj21*v5%=^_giqrbp&(j4t04dm(3ejx+383op(1ga'
DEBUG = True
ALLOWED_HOSTS: list[str] = []


# APLICACIONES

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    
    'main',
    'salones',
    'clientes',
    'reservas',
    'servicios',
    'pagos',
]


# MIDDLEWARE

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'salon_project.urls'


# TEMPLATES

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'salon_project.wsgi.application'


# BASE DE DATOS 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'salon_eventos',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
     
    }
}


# VALIDACIÓN DE CONTRASEÑAS

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# INTERNACIONALIZACIÓN

LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Guatemala'
USE_I18N = True
USE_TZ = True


# ARCHIVOS ESTÁTICOS

STATIC_URL = 'static/'
# Donde tienes /static/assets, /static/css, /static/js, etc.
STATICFILES_DIRS = [BASE_DIR / 'static']


# ID 

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
