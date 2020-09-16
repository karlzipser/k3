from k3 import *
from urllib.parse import unquote
from k3.drafts.htmltemp import *
kin = k_in_D

Arguments = get_Arguments(
    Defaults={
        'path':None,
        'URL_args':None,
    }
)

def main(**A):
    path = A['path']
    if path[0] == '/':
        path = path[1:]
        print("path = path[1:]")
    URL_args = A['URL_args']
    code = highlight(file_to_text(path), PythonLexer(), HtmlFormatter())
    s = head_('this is the title')
    s += style
    s += br*2
    s += l2h(d2n("You accessed path: ",path,''))
    s += br*2
    s += l2h(d2n("URL_args: ",str(URL_args),''))
    s += br*2


    s += '<h1>'+path+'</h1>'
    s += code

    s += 'end.'
    s += end_()    
    print(s)

if __name__ == '__main__':
    main(**Arguments)





#EOF
