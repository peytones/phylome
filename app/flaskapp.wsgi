#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/Projects/LANHacks/app/")

from FlaskApp import app as application
application.secret_key = 'dog'
