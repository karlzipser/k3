from k3 import *
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
from contextlib import redirect_stdout
import importlib
from k3.drafts.htmltemp import *

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
            path_to_image = opjh(self.path)[1:]
            statinfo = os.stat(path_to_image)
            img_size = statinfo.st_size
            self.send_response(200)
            self.send_header("Content-type", mimetype)
            self.send_header("Content-length", img_size)
            self.end_headers()
            if path_to_image not in Images:
                f = open(path_to_image, 'rb')
                cg('loading',path_to_image)
                Images[path_to_image] = f.read()
                f.close()
            self.wfile.write(Images[path_to_image])

        elif "favicon.ico" in self.path:
            return

        else:
            path,URL_args = urlparse(self.path)
            if path[0] == '/':
                path = path[1:]
            clear_screen()
            #d2s('url_path =',url_path)
            #zprint(URL_args)
            
            out = 'k3/__private__/__private.temp.txt'

            t0=time.time()

            os_system('python3',path,'--url',qtd(self.path),'>',out,e=1)

            #os_system("python3  k3/drafts/pages4.py --path k3/drafts/pages4.py --URL_args asd=vda >",out)

            print(time.time()-t0)

            self.send_response(200)

            self.send_header("Content-type", "text/html")

            self.end_headers()
 
            s = file_to_text("k3/__private__/__private.temp.txt")

            self.wfile.write(bytes(s, "utf-8"))



    def do_POST(self):
        '''Reads post request body'''
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        self.wfile.write("received post request:<br>{}".format(post_body))


myServer = ThreadingHTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))





#EOF
