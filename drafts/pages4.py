from k3 import *
from urllib.parse import unquote
from k3.drafts.htmltemp import *
kin = k_in_D

Arguments = get_Arguments(
    Defaults={
        'url':None,
    }
)
# http://localhost:9000/k3/drafts/pages4.py?a=b&c=d
def main(**A):
    path,URL_args = urlparse(A['url'])
    if path[0] == '/':
        path = path[1:]
        #print("path = path[1:]")
    code = highlight(file_to_text(path), PythonLexer(), HtmlFormatter())
    s = head_('this is the title')
    s += style
    s += br*2
    s += l2h(d2n("You accessed path: ",path,''))
    s += br*2


    for u in URL_args:
        s += l2h(d2n(u,': ',URL_args[u],'')) + br

    s += '<h1>'+path+'</h1>'
    s += code

    s += 'end.'
    s += end_()    
    print(s)

if __name__ == '__main__':
    main(**Arguments)





#EOF
