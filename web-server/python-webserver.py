#!/usr/bin/python3
import os 
os.chdir('/web/html')

#from flask_restful import Api, Resource
import http.server
import socketserver
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.path = '/index.html'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
Handler = MyRequestHandler
server = socketserver.TCPServer(('0.0.0.0', 8000), Handler)
server.serve_forever()