#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
from getState import *

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send message back to client
        # Write content as utf-8 data
        message = getState()
        self.wfile.write(bytes(message, "utf8"))
        return


def run():
    print('starting server...')

    # Server settings
    # Choose port 80
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()