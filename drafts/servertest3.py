from k3 import *
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
from contextlib import redirect_stdout
from urllib.parse import unquote
from k3.drafts.htmltemp import *
from k3.drafts.pages import *

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
            Z = {}
            a = self.path
            b = a.split('?')
            if len(b) > 1:
                c = b[-1]
                cg(c)
                d = c.split('&')
                for e in d:
                    if e is not None:
                        f = e.split('=')
                        print(f)
                        f[1] = f[1].replace('+',' ')
                        f[1] = unquote(f[1])
                        print(f[1])
                        Z[f[0]] = f[1]
            clear_screen()
            zprint(Z)

            self.send_response(200)

            self.send_header("Content-type", "text/html")

            self.end_headers()
 
            t0=time.time()
            import k3.utils.core.paths as k3_utils_core_paths
            with open("k3/__private__/__private.temp.txt", 'w') as f:
                with redirect_stdout(f):
                    print(time.time())
                    k3_utils_core_paths.main()

            print(time.time()-t0)


            if 'get_page' not in Z:
                Z['get_page'] = 'get_page0'
            s = G[Z['get_page']](self.path,Z)

            s += lines_to_html_str(file_to_text("k3/__private__/__private.temp.txt"))
            
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
