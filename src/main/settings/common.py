"""
Django settings for src project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), os.pardir))
print BASE_DIR

ADMINS = (
    ('Vitaliy', 'moskrc@gmail.com'),
)
MANAGERS=ADMINS

##################################################################################

sys.path.append(os.path.join(BASE_DIR, 'shared'))

DEBUG = True

ASSETS_DEBUG = TEMPLATE_DEBUG = DEBUG


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static_override'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

LOGOUT_URL = '/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',

    'main.context_processors.main_processor',
)


#################################################################################

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # 3rd party
    'south',
    'django_extensions',
    'markdown',
    'sorl.thumbnail',
    'compressor',
    
    'common',
    'catalog',
    'subscription',
    'feedback'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


ROOT_URLCONF = 'main.urls'

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'moskrc_jobs',
        'USER': 'moskrc_jobs',
        'PASSWORD': '1346795',
        'HOST': '',
        'PORT': ''
    }
}


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


COMPRESS_ROOT = BASE_DIR + '/static'

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

COMPRESS_PRECOMPILERS = (
       ('text/x-sass', '/home/moskrc/web/djangojobbers.ru/private/env/bin/pyscss {infile} > {outfile}'),
)

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = None

##################################################################################


if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'test.db3'}
    SOUTH_TESTS_MIGRATE = False

##################################################################################
