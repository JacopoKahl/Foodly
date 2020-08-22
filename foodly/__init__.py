from __future__ import absolute_import

# The app is imported on every Django start
from .celery import app as celery_app