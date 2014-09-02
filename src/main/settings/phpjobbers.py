# -*- coding: utf-8 -*-

from common import *

SITE_ID = 3

try:
    from phpjobbers_local import DEBUG
except ImportError:
    DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'phpjobbers.ru']

SERVER_EMAIL = DEFAULT_FROM_EMAIL = 'noreply@phpjobbers.ru'
EMAIL_SUBJECT_PREFIX = '[phpjobbers.ru] '
EMAIL_HOST_USER = 'noreply@phpjobbers.ru'
EMAIL_HOST_PASSWORD = '1346795'
DEFAULT_FROM_EMAIL='noreply@phpjobbers.ru'


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/per_sites/phpjobbers'),
    os.path.join(BASE_DIR, 'templates'),
)

try:
    from phpjobbers_local import *
except NameError:
    pass

if not SECRET_KEY:
    raise Exception('You must to provide SECRET_KEY value in phpjobbers_local.py')

