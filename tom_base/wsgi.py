"""
WSGI config for tom_base project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ["DJANGO_SETTINGS_MODULE"] = "tom_base.settings"
os.environ['HTTPS'] = "on"
os.environ['TOM_NAME'] = ""
os.environ['TOM_USER'] = ""
os.environ['TOM_PASSWORD'] = ""
os.environ['TOM_HOST'] = ""
os.environ['TOM_PORT'] = ""

_application = get_wsgi_application()

env_variables_to_pass = ['TOM_USER']

def application(environ, start_response):
    # pass the WSGI environment variables on through to os.environ
    for var in env_variables_to_pass:
        os.environ[var] = environ.get(var, '')
    return _application(environ, start_response)
