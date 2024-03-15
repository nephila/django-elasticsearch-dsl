import django

from django.utils.module_loading import autodiscover_modules

from .documents import Document  # noqa
from .indices import Index  # noqa
from .fields import *  # noqa

__version__ = '2.0.0'


def autodiscover():
    autodiscover_modules('documents')


