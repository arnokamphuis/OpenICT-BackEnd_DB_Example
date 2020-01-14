#! /usr/bin/python3.5

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '<path to current folder>')
from backend import app as application
application.secret_key = 'kapper'
