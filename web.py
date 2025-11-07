from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"User ver 1.0.0")

if __name__ == "__main__":
    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, HelloHandler)
    print("Server đang chạy tại http://0.0.0.0:8000")
    httpd.serve_forever()
