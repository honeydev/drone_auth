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
                'NAME': os.getenv('POSTGRES_DB', 'vacation_visualiser'),
                'USER': os.getenv('POSTGRES_USER', 'vacation_visualiser'),
                'PASSWORD': os.getenv(
                    'POSTGRES_PASSWORD',
                    'vacation_visualiser'
                ),
                'HOST': os.getenv('POSTGRES_HOST', 'postgres'),
                'PORT': os.getenv('POSTGRES_PORT', '5432'),
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
