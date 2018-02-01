import time
import http.server as BaseHTTPServer


HOST_NAME = '127.0.0.1' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 852 # Maybe set this to 9000.


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write(bytes("<html><head><title>Title goes here.</title></head>","utf8"))
        s.wfile.write(bytes("<body><p>This is a test.</p>","utf8"))
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        s.wfile.write(bytes("<p>You accessed path: %s</p>" % s.path, "utf8"))
        s.wfile.write(bytes("</body></html>","utf8"))

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print( time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print (time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))