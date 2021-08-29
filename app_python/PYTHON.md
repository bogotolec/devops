# TL;DR

Simplest http server that shows current time, nothing special.

## Framework

Since this application is extremely simple to design, I decided to use default python libraries `http.server` for serving content, and `datetime` for recieving information about current time.

## Code style

For this project I have used default python code style [PEP 8](https://www.python.org/dev/peps/pep-0008/) with four spaces for indentation.

## Unit tests

File `test.py` contains code for 2 unit tests: test of the time getting and test of the http handler.

### TestTimeReciever

This test checks if my module of time recieving produce a string which shows time with precision of 120 seconds.

### TestMyHttpHandler

This test tries to create a simple http server with my custom http handler, and, if it is creating successfully, then test will be passed. 