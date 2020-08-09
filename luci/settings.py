"""
LUCI settings module.
"""
from decouple import config

__version__ = '0.1.5'

TOKEN = config('TOKEN', '')
BACKEND_URL = config('BACKEND_URL', '')
LISA_URL = config('LISA_URL', '')
SETTINGS_MODULE = config('SETTINGS_MODULE', 'common')
