import os

DEBUG=True

SECRET_KEY = 'Xxw1*2avipkt9asqv#_&ampRaxte-0#f0)j()i@jf!(zg8v#(!p(6e'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '../src/djangojobbers.log',
            'maxBytes': 1024 * 1024 * 5, # 5 MB
            'backupCount': 5,
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins','file','console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'project': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },

    }
}
