import unittest
from datetime import datetime
from server import MyHttpHandler, TimeReciever
from http.server import HTTPServer

class TestTimeReciever(unittest.TestCase):

    def test_time_recieving(self):
        testtime = TimeReciever.get_time()
        testtime = datetime.strptime(testtime, "%A, %d. %B %Y %I:%M%p")

        truetime = datetime.now()

        diff = testtime - truetime
        diff_in_seconds = abs(diff.total_seconds())

        self.assertLess(diff_in_seconds, 120)


class TestMyHttpHandler(unittest.TestCase):

    def test_server_creation(self):

        server = HTTPServer(('localhost', 8888), MyHttpHandler)
        server.timeout = 2
        server.handle_request()
        server.server_close()

if __name__ == "__main__":
    unittest.main()
