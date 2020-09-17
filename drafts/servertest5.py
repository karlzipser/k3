from k3 import *
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
from contextlib import redirect_stdout
import importlib
from k3.drafts.htmltemp import *

hostName = "localhost"
hostPort = 9000
Images = {}

import re

# 7-bit C1 ANSI sequences
ansi_escape = re.compile(r"""
    \x1B  # ESC
    (?:   # 7-bit C1 Fe (except CSI)
        [@-Z\\-_]
    |     # or [ for CSI, followed by a control sequence]
        \[
        [0-?]*  # Parameter bytes
        [ -/]*  # Intermediate bytes
        [@-~]   # Final byte
    )
""", re.VERBOSE)
#result = ansi_escape.sub('', sometext)

a = get_list_of_files_recursively(opjk('utils'),'*.py')
b = []
for c in a:
    #if fname(a)[0] == '_':
    #    continue
    b.append('/'+c.replace(opjh(),''))
paths = sorted(b)

Imports = {}
print('Sart Imports...')
for p in paths:
    try:
        if p[0] == '/':
            p = p[1:]
        m = opj(pname(p),fnamene(p)).replace('/','.')
        Imports[p] = importlib.import_module( opj(pname(p),fnamene(p)).replace('/','.') ) 
        Imports[p+':time'] = time.time()
    except:
        print(p,'failed')
print('Imports done.')
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

            path, URL_args = urlparse(self.path)

            if path not in paths:
                path = paths[0]
                redirect = """<meta http-equiv="Refresh" content="0; url='"""+path+"""'" />"""
            else:
                redirect = ''
            p = path
            if p[0] == '/':
                p = p[1:]
            

            raw_code = file_to_text(p)
            code = highlight(raw_code, PythonLexer(), HtmlFormatter())
            out = 'k3/__private__/__private2.temp.txt'

            if 'def main(**' in raw_code:

                with open(out, 'w') as f:
                    with redirect_stdout(f):
                        if os.path.getmtime(p) > Imports[p+':time']:
                            importlib.reload( Imports[p] )
                            Imports[p+':time'] = time.time()
                        Imports[p].main(**URL_args)
            else:
                cm('python3',p,'--url',self.path,'>',out,r=0)
                os_system('python3',p,'--url',qtd(self.path),'>',out)









            s = head_('this is the title')
            s += style
            s += """<div style="font-family:'Courier New';font-size:12px">"""
            ctr = 0
            q = 40
            for p in paths:
                if 'has' in URL_args:
                    if URL_args['has'] not in p:
                        continue
                # +"?a=b&c=d"
                url = p+'?has=utils/core'
                s += href_(p,p[:min(q,len(p))]) + max(0,(q-len(p)))*sp
                ctr += 1
                if ctr%3 ==0:
                    s += br
            s += '<h1>'+path+'</h1>'
            s += '<h2>'+'output'+'</h2>'

            s += highlight(
                ansi_escape.sub('', file_to_text(out)),
                PythonLexer(),
                HtmlFormatter())

            s += br*2
            
            s += '<h3>'+'URL_args'+'</h3>'
            s_ = 'path: '+path +'\n'
            for u in URL_args:
                s_ += d2n(u,': ',URL_args[u]) +'\n'
            s += highlight(s_, PythonLexer(), HtmlFormatter())

            s += '<h2>'+'code'+'</h2>'
            s += code
            s += redirect

            s += "</div>"
            s += 'end.'

            s += end_()

            print(s)


            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
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
