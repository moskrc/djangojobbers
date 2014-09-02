# -*- coding: utf-8 -*-

from common import *

try:
    from djangojobbers_local import DEBUG
except ImportError:
    DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'djangojobbers.ru']

SERVER_EMAIL = DEFAULT_FROM_EMAIL = 'noreply@djangojobbers.ru'
EMAIL_SUBJECT_PREFIX = '[djangojobbers.ru] '


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/per_sites/djangojobbers'),
    os.path.join(BASE_DIR, 'templates'),
)

try:
    from djangojobbers_local import *
except NameError:
    pass

if not SECRET_KEY:
    raise Exception('You must to provide SECRET_KEY value in djangojobbers_local.py')

SITE_ID = 1
