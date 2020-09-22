from k3 import *
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
from contextlib import redirect_stdout
import importlib

from htmlpy import *

def trim_paths(paths):
    paths = sorted(paths)
    q = []
    for p in paths:
        q.append(p.replace(opjk(),'').split('/'))

    for i in range(len(q)-1,1,-1):
        for j in rlen(q[i]):
            print(i,j)
            try:
                if q[i][j] == q[i-1][j]:
                    q[i][j] = ' '*len(q[i][j])
            except:
                pass
    r = []
    for u in q:
        r.append('/'.join(u).replace(
            '/ ','  ').replace(opjk(),'').replace(' /','  '))
    return r


a = get_list_of_files_recursively(opjk(''),'*.py')
b = []
for c in a:
    #if fname(a)[0] == '_':
    #    continue
    b.append('/'+c.replace(opjh(),''))
paths = sorted(b)
s = ''
ctr = 0
for pp,pr in zip(trim_paths(paths),paths):
    url = pp
    s += href_(pr,pp[1:].replace(' ','&nbsp'),False)
    ctr += 1
    if True:#ctr%3 ==0:
        s += br
files = s
#text_to_file(opjD('paths.txt'),s)


hostName = "localhost"
hostPort = 9000
Images = {}
SubCode = {
    '---ACE-ACE---':    opjk('utils/html/ace/ace.js'),
    '---ACE-MODE---':   opjk('utils/html/ace/mode-python.js'),
    '---ACE-THEME---':  opjk('utils/html/ace/theme-twilight.js'),
    '---WEBPAGE---':    opjk('utils/html/webpage.html'),
    '---EDITOR---':     opjk('utils/core/paths.py'),
    '---FILES---':      (files,),
    '---FIGURES---':    (
"""<img src="/Desktop/Internet_dog.jpg" style="width:600px;">""",),
    '---OUTPUT---':    (
"""ELIZA is an early natural language processing computer program created from 1964 to 1966[1] at the MIT Artificial Intelligence Laboratory by Joseph Weizenbaum.[2] Created to demonstrate the superficiality of communication between humans and machines, Eliza simulated conversation by using a "pattern matching" and substitution methodology that gave users an illusion of understanding on the part of the program, but had no built in framework for contextualizing events.[3][4] Directives on how to interact were provided by "scripts", written originally in MAD-Slip, which allowed ELIZA to process user inputs and engage in discourse following the rules and directions of the script. The """,),

}

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
        
            html = '---WEBPAGE---'

            ks = kys(SubCode)
            #cg(ks)
            ks.remove(html)#('---WEBPAGE---')
            #cb(ks)
            ks = [html]+ks#['---WEBPAGE---'] + ks

            for j in ks:
                if type(SubCode[j]) is str:
                    #cm(SubCode[j],r=1)
                    r = file_to_text(SubCode[j])
                else:
                    #cb(SubCode[j],r=1)
                    assert type(SubCode[j]) is tuple
                    r = SubCode[j][0]
                html = html.replace(j,r)
            
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(html, "utf-8"))






myServer = ThreadingHTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))





#EOF
