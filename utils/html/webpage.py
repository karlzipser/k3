from k3 import *
from htmlpy import *
import tree_

SubCode = {
    '---ACE-ACE---':    opjk('utils/html/ace/ace.js'),
    '---ACE-MODE---':   opjk('utils/html/ace/mode-python.js'),
    '---ACE-THEME---':  opjk('utils/html/ace/theme-twilight.js'),
    '---WEBPAGE---':    opjk('utils/html/webpage.html'),
    #'---EDITOR---':     "nothing",#opjk('utils/core/paths.py'),
    '---REDIRECT---':   '',
    't--FIGURES---':    
            """<img src="/Desktop/Internet_dog.jpg" style="width:600px;">""",
    't--OUTPUT---':"""
<form>
  <input style="font-size:25px;font-weight:bold;" type="text" id="file" name="file" value="k3/utils/core/paths.py">
  <label for="file">file</label>
  <br>
  <input style="font-size:14px;" type="text" id="src" name="src" value="Pictures/new">
  <label for="src">--src</label>
  <br>
  <input style="font-size:14px;" type="text" id="dst" name="dst" value="Desktop/samples">
  <label for="dst">--dst</label>
  <br>
  <input style="font-size:14px;" type="text" id="extra" name="extra" value="">
  <label for="extra">additional cmd line str</label>
  <br>
  <input type="submit" value="Submit">
</form>
    """,
    
}



def _get_files(path=opjk('utils')):
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
    return files,paths


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



def handle_path_and_URL_args(p,URL_args):

    if 'SaveCode' in URL_args:
        sc = URL_args['SaveCode'].replace('\r','')
        os_system('mv',p,d2p(p,time.time()))
        text_to_file(p,sc) 


def get_SubCode(url):
    path, URL_args = urlparse(url)
    cm(path)
    p = path
    del path
    if p[0] == '/' and len(p) > 1:
        p = p[1:]

    if not os.path.isfile(p):
        p_ = p
        p = opjk('utils/__init__.py').replace(opjh(),'')
        cr(p_,'-->',p,r=0)

    handle_path_and_URL_args(p,URL_args)
    SubCode['t--URL_args---'] = print_dic_simple(URL_args,'',html=True)
    try:
        if len(sggo(p)) == 1:
            SubCode['---EDITOR---'] = p
    except:
        pass

    #SubCode['---FILES---'],paths = _get_files()
    if False:#path not in paths:
        SubCode['t--REDIRECT---'] = \
            """<meta http-equiv="Refresh" content="0; url='"""+ \
            path+"""'" />"""
    #SubCode['---OUTPUT---'] = d2s(path,URL_args)
    SubCode['t--TITLE---'] = p # this so not treated as path
    SubCode['t--FILES---'] = tree_.get_tree(p)
    cm(SubCode['t--FILES---'])
    SubCode['t--PATH-URL---'] = p + '?' + urlencode(URL_args)
    clp(SubCode['t--PATH-URL---'],'`rwb')
    return SubCode

#EOF
