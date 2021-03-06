"""
Django settings for redly project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'core/static/js', 'serviceworker.js')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zmp$e1z@p-+#zqx21$oc!3o%blm#zxvmxi3i#4siwzxx@-m=n0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'core',
    'rest_framework',
    'djangobower',
    'redweb',
    'compressor',
    'webapimd',
    'pwa',
    # 'livereload',
    # 'rest_auth',
    # 'rest_framework.authtoken',
    # 'channels',
]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'redly.urls'

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

WSGI_APPLICATION = 'redly.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'compressor.finders.CompressorFinder',
)
#
# COMPRESS_ENABLED = True
# COMPRESS_URL = '/static/'
#
# COMPRESS_PRECOMPILERS = (
#     ('text/x-scss', 'core.compressor_filters.PatchedSCSSCompiler'),
# )
#
# COMPRESS_CSS_FILTERS = (
#     'core.compressor_filters.CustomCssAbsoluteFilter',
# )
# BOWER_INSTALLED_APPS = (
#     'bootstrap-sass-official#3.3.1',
# )

AUTH_USER_MODEL = 'core.User'
LOGIN_URL='/login'
LOGIN_REDIRECT_URL='/redly/'
LOGOUT_REDIRECT_URL='/redly/'
CORS_ORIGIN_ALLOW_ALL = True

#CORS_ORIGIN_WHITELIST = (
#    '127.0.0.1:8100',
#    'http://127.0.0.1:8100',
#    'http://localhost:8100/',
#    'localhost:8100'
#)
# CHANNEL_LAYERS = {
#     'default' : {
#         'BACKEND' : 'asgiref.inmemory.ChannelLayer',
#         'ROUTING' : 'redweb.routing.channel_routing',
#     }
# }
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    )
}

PWA_APP_NAME = 'Redly'
PWA_APP_DESCRIPTION = "Redly é uma rede social destinada a todos, tem foco principal a escolas e empresa"
PWA_APP_THEME_COLOR = '#ad0a18'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_ICONS = [
    {
        'src': '/static/imagem/icons/256.png',
        'sizes': '256x256'
    },
    {
        'src': '/static/imagem/icons/192.png',
        'sizes': '192x192'
    },
    {
        'src': '/static/imagem/icons/512.png',
        'sizes': '512x512'
    }
]
PWA_APP_START_URL = '/redly/'
