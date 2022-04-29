from library.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memorydb_default:',
    }
}

MIGRATIONS_MODULES = None

MIGRATE = False
