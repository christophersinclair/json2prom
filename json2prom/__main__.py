import logging

from waitress import serve

import _constants as const

from json2prom import app

host = const.API_HOST
port = const.API_PORT
threads = const.NUM_THREADS
channel_timeout = const.CHANNEL_TIMEOUT

welcome_message = f"Waitress server started. Serving requests on host {host}, port {port} with {threads} threads and a timeout of {channel_timeout}s..."

if __name__ == "__main__":
    print(welcome_message)
    logging.info(welcome_message)
    serve(app, host=host, port=port, threads=threads, channel_timeout=channel_timeout)