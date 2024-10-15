import logging
from waitress import serve
from app import app
from paste.translogger import TransLogger

app_logged = TransLogger(app, setup_console_handler=True)

print("iniciei o servidor WSGI")

if __name__ == '__main__':
    serve(
        app_logged,
        host='0.0.0.0',
        port=7777,
        trusted_proxy='*', # Ips permitidos devem ser separados por espacos * para qualquer 1
        trusted_proxy_headers='x-forwarded-for x-forwarded-proto x-forwarded-host x-forwarded-port'
    )
