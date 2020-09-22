from htmlpy import *

SubCode = {
    '---TITLE---':      'page title',
    '---ACE-ACE---':    opjk('utils/html/ace/ace.js'),
    '---ACE-MODE---':   opjk('utils/html/ace/mode-python.js'),
    '---ACE-THEME---':  opjk('utils/html/ace/theme-twilight.js'),
    '---WEBPAGE---':    opjk('utils/html/webpage.html'),
    '---EDITOR---':     opjk('utils/core/paths.py'),
    '---FIGURES---':    
"""<img src="/Desktop/Internet_dog.jpg" style="width:600px;">""",
    '---OUTPUT---':    
"""ELIZA is an early natural language processing computer program created from 
1964 to 1966[1] at the MIT Artificial Intelligence 
Laboratory by Joseph Weizenbaum.[2] Created to demonstrate the superficiality 
of communication between humans and machines, Eliza simulated conversation by 
using a "pattern matching" and substitution methodology that gave users an
 illusion of understanding on the part of the program, but had no built in 
 framework for contextualizing events.[3][4] Directives on how to interact 
 were provided by "scripts", written originally in MAD-Slip, which allowed 
 ELIZA to process user inputs and engage in discourse following the rules and 
 directions of the script. The """,
}



def _get_files(path=opjk('')):
    a = get_list_of_files_recursively(path,'*.py')
    b = []
    for c in a:
        b.append('/'+c.replace(opjh(),''))
    paths = sorted(b)
    files = ''
    ctr = 0
    for pp,pr in zip(_trim_paths(paths),paths):
        url = pp
        files += href_(pr,pp[1:].replace(' ','&nbsp'),False)
        ctr += 1
        files += br
    return files


def _trim_paths(paths):
    paths = sorted(paths)
    q = []
    for p in paths:
        q.append(p.replace(opjk(),'').split('/'))

    for i in range(len(q)-1,1,-1):
        for j in rlen(q[i]):
            #print(i,j)
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



def handle_path_and_URL_args(path,URL_args):
    pass

def get_SubCode(url):
    path, URL_args = urlparse(url)
    handle_path_and_URL_args(path,URL_args)

    p = path
    if p[0] == '/' and len(p) > 1:
        p = p[1:]
    try:
        if len(sggo(p)) == 1:
            SubCode['---EDITOR---'] = p
    except:
        pass


    SubCode['---FILES---'] = _get_files()
    SubCode['---OUTPUT---'] = d2s(path,URL_args)
    SubCode['---TITLE---'] = p # this so not treated as path
    return SubCode

#EOF
