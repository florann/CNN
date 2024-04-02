# Python 3 server example
from functools import cached_property
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qsl, urlparse

import string

import time

pathPage = "./Server/Pages/"

class WebRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        #Getting the page name
        splitedUrl = self.url.path.split("/",1)
        print(splitedUrl)
        pageRequest = pathPage+splitedUrl[1]

        #Using context manager to access to the file
        with open(pageRequest) as file:
            #Getting the content
            content = file.read()
            #Writing it
            self.wfile.write(content.encode('utf-8'))


    @cached_property
    def url(self):
        return urlparse(self.path)

    @cached_property
    def query_data(self):
        return dict(parse_qsl(self.url.query))

    @cached_property
    def post_data(self):
        content_length = int(self.headers.get("Content-Length", 0))
        return self.rfile.read(content_length)

    @cached_property
    def form_data(self):
        return dict(parse_qsl(self.post_data.decode("utf-8")))
