# main project dependencies providers module

import os

from django.conf import settings


def db_provider():
    """Provide database backend."""

    db_backend = os.getenv('DB_BACKEND', 'sqlite3').lower().strip()

    if db_backend == 'pg':
        return {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.getenv('DB_NAME', 'drone_auth'),
                'USER': os.getenv('DB_USER', 'drone_auth'),
                'PASSWORD': os.getenv(
                    'DB_PASSWORD',
                    'drone_auth'
                ),
                'HOST': os.getenv('DB_HOST', 'localhost'),
                'PORT': os.getenv('DB_PORT', '5432'),
            },
        }
    elif db_backend == 'sqlite3':
        return {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(
                    settings.BASE_DIR,
                    os.getenv('DB_NAME', 'db.sqlite3')
                ),
            }
        }

    raise ValueError(f'Invalid db backend {db_backend}')
