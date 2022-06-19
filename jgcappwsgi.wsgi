import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.append('/var/www/html/jgcapp/venv/lib/python3.6/site-packages')
sys.path.append('/var/www/html/jgcapp')

from app import app as application
application.secret_key= "Add your key"


