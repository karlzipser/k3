from k3 import *
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
hostPort = 9000
Images = {}
class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        mimetype=None
        if exname(self.path) in ('jpeg','jpg','JPG','JPEG'):
            mimetype='image/jpg'
        elif exname(self.path) in ('png','PNG'):
            mimetype='image/png'
        elif exname(self.path) in ('gif','GIF'):
            mimetype='image/gif'

        if mimetype is not None:      
            path_to_image = opjh(self.path)[1:]#fname(self.path))#opjh("img.jpeg")
            statinfo = os.stat(path_to_image)
            img_size = statinfo.st_size
            self.send_response(200)
            self.send_header("Content-type", mimetype)
            self.send_header("Content-length", img_size)
            self.end_headers()
            if path_to_image not in Images:
                f = open(path_to_image, 'rb')
                Images[path_to_image] = f.read()
                f.close()
                #print(type(Images[path_to_image]))
                #mi(np.frombuffer(Images[path_to_image],np.uint8),path_to_image)#+time_str())
            self.wfile.write(Images[path_to_image])
              
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
            self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
            self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes(time_str('Pretty2'), "utf-8"))
            self.wfile.write(bytes("""<br><img src="img.jpeg" style="width:200px;"><br><br>""", "utf-8"))
            self.wfile.write(bytes("""<br><img src="Desktop/IMG_1778.JPG" style="width:200px;"><br><br>""", "utf-8"))
            self.wfile.write(bytes("""

<form action="search" method="GET">
Search Term: <input type="text" name="search_query">
</form>
<br>

<form action="" method="get">
    <input type="submit" name="upvote" value="Upvote" />
</form>
<br><img src="Desktop/img.png" style="width:200px;"><br><br>""", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))

    def _do_GET(self):
        path_to_image = opjh("img.jpeg")
        statinfo = os.stat(path_to_image)
        img_size = statinfo.st_size
        self.send_response(200)
        self.send_header("Content-type", "image/jpg")
        self.send_header("Content-length", img_size)
        self.end_headers()
        f = open(path_to_image, 'rb')
        self.wfile.write(f.read())
        f.close()   


    def do_POST(self):
        '''Reads post request body'''
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        self.wfile.write("received post request:<br>{}".format(post_body))


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))





# https://riptutorial.com/python/example/26748/basic-handling-of-get--post--put-using-basehttprequesthandler

