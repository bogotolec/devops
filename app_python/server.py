from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

ADDR = ("localhost", 8888)

class TimeReciever:
    def get_time():
        return datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

def get_visits():
    with open("logs/visits.txt", "r") as o:
        return o.read()

def inc_visits():
    current = int(get_visits())
    current += 1
    with open("logs/visits.txt", "w") as w:
        w.write(str(current))

def create_visits():
    with open("logs/visits.txt", "w") as w:
        w.write("0")

class MyHttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):


        # Send status code, since we don't operate on
        # any data, we always send 200 (OK).
        self.send_response(200)

        # Send usual headers for text web pages.
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        content = ""

        if self.path == "/visits":
            content = get_visits().encode('utf-8')
        else:
            inc_visits()
            content = TimeReciever.get_time().encode('utf-8')

        self.wfile.write(content)


if __name__ == '__main__':
    create_visits()
    server = HTTPServer(ADDR, MyHttpHandler)
    server.serve_forever()
