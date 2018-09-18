import http.server
import socketserver

PORT = 8000

jclass myHTTPServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print("command is ",self.command)
        print("path is ",self.path)
        if (self.path == "/test"):
            print("triggered override of method")
        super().do_GET()
        
    def do_POST(self):
        print("command is ",self.command)
        print("path is ",self.path)
        if (self.path == "/ajax-get"):
            print ("received POST:/ajax-get | I should make an ajax response")
            self.send_response(200)
            self.send_header('Content-type','application/xml')
            self.end_headers()
            #string literals are prefixed with 'b' to indicate utf-8 encoding
            self.wfile.write(b"<?xml version='1.0'?>")
            self.wfile.write(b"<name>value</name>")
            
Handler = myHTTPServer

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
    