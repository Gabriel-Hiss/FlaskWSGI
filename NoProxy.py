import logging
from waitress import serve
from app import app
from paste.translogger import TransLogger


logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

app_logged = TransLogger(app, setup_console_handler=True)

print("iniciei o servidor WSGI")

if __name__ == '__main__':
    serve(app_logged, host='0.0.0.0', port=5000)
