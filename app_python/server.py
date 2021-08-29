from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

ADDR = ("localhost", 8888)

class TimeReciever:
    def get_time():
        return datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

class MyHttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        # Send status code, since we don't operate on
        # any data, we always send 200 (OK).
        self.send_response(200)

        # Send usual headers for text web pages.
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        time = TimeReciever.get_time()

        self.wfile.write(time.encode('utf-8'))


if __name__ == '__main__':
    server = HTTPServer(ADDR, MyHttpHandler)
    server.serve_forever()
