from social.backends.utils import load_backends
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'asholok'))

import settings

PREPARED_BACKENDS = load_backends(settings.AUTHENTICATION_BACKENDS)