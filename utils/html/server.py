from k3 import *
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
Arguments = get_Arguments(
    {'webpage':'k3.utils.html.webpage'}
)
exec(d2s('import',Arguments['webpage'],'as wp'))

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
        
            SubCode = wp.get_SubCode(self.path)

            html = '---WEBPAGE---'

            ks = kys(SubCode)
            ks.remove(html)
            ks = [html] + ks

            for j in ks:
                sc = SubCode[j]
                sc_is_path = False
                try:
                    if len(sggo(sc)) == 1:
                        sc_is_path = True
                except:
                    pass
                if sc_is_path:
                    cg('treating',j,sc,'as path')
                    r = file_to_text(SubCode[j])
                else:
                    cb('treating',j,'as text')
                    r = SubCode[j]
                html = html.replace(j,r)
            
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(html, "utf-8"))



def main(**A):

    hostName = "localhost"
    hostPort = 9000

    myServer = ThreadingHTTPServer((hostName, hostPort), MyServer)
    print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

    try:
        myServer.serve_forever()
    except KeyboardInterrupt:
        pass

    myServer.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))


if __name__ == '__main__':
    main()



#EOF
