from k3 import *
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
import time
from urllib.parse import unquote
from k3.drafts.htmltemp import *


hostName = "localhost"
hostPort = 9000
Images = {}
ctr = 0

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        global ctr
        #print("def do_GET(self):")
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


        else:
            if "favicon.ico" in self.path:
                #cr(self.path,r=0)
                return

            clear_screen()

            self.send_response(200)

            self.send_header("Content-type", "text/html")
            self.end_headers()

            s = head_('this is the title')

            ctr += 1

            if ctr > 10:
                s = 'This is the end.'
            
            else:

                s += l2h(d2n("You accessed path: ",self.path,''))

                s += br*2

                s += l2h(d2n("You accessed path: ",unquote(self.path)))

                z = {}
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
                            z[f[0]] = f[1]
                zprint(z)
                    
                s += br*2
                
                s += l2h('   some text! •¶§∞¢')

                s += br

                s += href_(
                    '/',
                    img_('Desktop/a.png',"width:200px;"), 
                )

                s += br

                s += href_('?path=ads/bfe/ca/','suck it up')

                s += br

                s += href_(
                    '?this_images_points_to=this_text&q=w&n=1',
                    img_('Desktop/b.png',"width:200px;"), 
                )

                s += br

                s += href_("?a=a/b/c/",'suck it up 2')

                s += br

                s += form_('what the heck?')

                s += br

                #s += "print%281%2Ba%29 "

                s += br

            s += end_()
 
            #print(s)
            
            self.wfile.write(bytes(s, "utf-8"))
            print(ctr)
            if ctr > 10:
                assert(0)

    def do_POST(self):
        '''Reads post request body'''
        #print("def do_POST(self):")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        self.wfile.write("received post request:<br>{}".format(post_body))


#myServer = HTTPServer((hostName, hostPort), MyServer)
myServer = ThreadingHTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))


"""
<form action="" method="get">
    <input type="submit" name="upvote" value="Upvote" />
</form>
<a href="abc">lh</a>


"""


# https://riptutorial.com/python/example/26748/basic-handling-of-get--post--put-using-basehttprequesthandler

