#!/usr/bin/python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
PATH = ""

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        global PATH
        PATH = self.path

class LocalHost():
    def __init__(self, localhost = 'localhost', port = 49999):
        server_address = (localhost, port)
        self.httpd = HTTPServer(server_address, RequestHandler)

    def getResponse(self, timeout = 40):
        self.httpd.timeout = timeout
        self.httpd.handle_request()

    def getCode(self):
        global PATH
        print(PATH)
        print(parse_qs(PATH))
        code = parse_qs(PATH)['/?code'][0]
        text = PATH.split('/?code')
        PATH = text[0]
        return code

    def killLocalHost(self):
        self.httpd.server_close()