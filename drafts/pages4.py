from k3 import *
from urllib.parse import unquote
from k3.drafts.htmltemp import *

# http://localhost:9000/k3/drafts/pages4.py?a=b&c=d

Arguments = get_Arguments(
    Defaults={
        'url':None,
    }
)
paths = [
    #'k3/scripts/gen/temperature.py',
    'k3/utils/core/printing.py',
    'k3/utils/core/paths.py',
]

def main(**A):
    path, URL_args = urlparse(A['url'])
    cb(path)

    code = highlight(file_to_text(path), PythonLexer(), HtmlFormatter())
    #script = path
    #clear_screen()
    out = 'k3/__private__/__private2.temp.txt'
    os_system('python3',path,'--url',qtd(A['url']),'>',out)

    s = head_('this is the title')
    s += style
    s += href_("'/k3/utils/core/printing.py?a=b&c=d'",'k3/utils/core/printing.py')
    s += '<h1>'+path+'</h1>'
    s += '<h2>'+'output'+'</h2>'

    #s += l2h(file_to_text("k3/__private__/__private2.temp.txt"))
    s += highlight(
        file_to_text("k3/__private__/__private2.temp.txt"),
        PythonLexer(),
        HtmlFormatter())

    s = s.replace('IN',"<strong><font color='green'>In</font></strong>")
    s = s.replace('OUT',"<strong><font color='red'>Out</font></strong>")

    s += br*2
    
    s += '<h3>'+'URL_args'+'</h3>'
    s_ = 'path: '+path +'\n'
    for u in URL_args:
        s_ += d2n(u,': ',URL_args[u]) +'\n'
    s += highlight(s_, PythonLexer(), HtmlFormatter())

    s += '<h2>'+'code'+'</h2>'
    s += code

    s += 'end.'

    if False:#path not in paths:
        cy('here',r=1)
        path = 'k3/utils/core/paths.py'
        #s += "<meta http-equiv='refresh' content='time; URL="+path+'/>'
        

    s += end_()

    print(s)

if __name__ == '__main__':
    main(**Arguments)



#http://localhost:9000/k3/utils/core/paths.py?a=1&b=2&c=3

#EOF
