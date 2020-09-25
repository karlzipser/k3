from k3 import *
from htmlpy import *
import tree_
import importlib
from contextlib import redirect_stdout
import html

D = {
    'files_dir':opjk('utils'),
}
Imports = {}
SubCode = {
    '---ACE-ACE---':    opjk('utils/html/ace/ace.js'),
    '---ACE-MODE---':   opjk('utils/html/ace/mode-python.js'),
    '---ACE-THEME---':  opjk('utils/html/ace/theme-twilight.js'),#opjk('utils/html/ace/theme-iplastic.js'),#
    '---WEBPAGE---':    opjk('utils/html/webpage.html'),
    't--FIGURES---':    
            """<img src="/Desktop/Internet_dog.jpg" ;">""",
    
    
}
# create dynamic output tab
# add imports and mtime reloads
# sort out problem with directory to dic
# run


def get_Output_form(p,A):
    s = """
   <form>
   """
    """
      <input readonly style="font-size:25px;font-weight:bold;" type="text" id="file_output" name="file_output" value=\""""+p+"""\">
      <label for="file">file</label>
      <br>
    """
    #s = ''
    for k in A.keys():
        k_ = k + '_output'
        s += """
  <input style="font-size:14px;" type="text" id=\""""+k_+"""\" name=\""""+k_+"""\" value=\""""+A[k]+"""\">
  <label for=\""""+k_+"""\">--"""+k+"""</label>
  <br>
    """

    s += """
  <input spellcheck="false" style="font-size:14px;" type="text" id="extra_output" name="extra_output" value="">
  <label for="extra_output">additional cmd line str</label>
  <br>
  """

    s += """
  <input hidden readonly type="text" id="run_output" name="run_output" value=\"Run\">
    """
    s += """
  <input hidden readonly type="text" id="city_tab" name="city_tab" value=\"Output\">
    """    
    s += """
  <input type="submit" value="Run">
  </form>
    """
    return s






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
        files += href_(pr+'abc'+'?city_tab=Files',pp[1:].replace(' ','&nbsp'),False)
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
        from bs4 import BeautifulSoup
        if not bool(BeautifulSoup(URL_args['SaveCode'], "html.parser").find()):
            sc = URL_args['SaveCode'].replace('\r','')
            n = opjh('bkps',p.replace(opjh(),''))
            cr(n)
            os_system('mkdir -p',pname(n))
            os_system('mv',p,d2p(n,time.time()))
            text_to_file(p,sc)
            if len(URL_args['SaveCode']) > 50:
                URL_args['SaveCode'] = URL_args['SaveCode'][:50]+' . . .'
        else:
            print("Can't save because URL_args['SaveCode'] contains html")
            #print(qtd(URL_args['SaveCode']))
    if p not in Imports:
        Imports[p] = importlib.import_module( opj(pname(p),fnamene(p)).replace('/','.') ) 
        Imports[p+':time'] = time.time()
        cb('imported',p)

    if os.path.getmtime(p) > Imports[p+':time']:
        importlib.reload( Imports[p] )
        Imports[p+':time'] = time.time()
        cb('reloaded',p)

    try:
        zprint(Imports[p].Arguments,'Arguments')
    except:
        cb('p has no Arguments')
    #Imports[p].main(**URL_args)

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

    try:
        A = Imports[p].Arguments
    except:
        A = {}
    SubCode['t--OUTPUT---'] = get_Output_form(p,A)

    if False:#path not in paths:
        SubCode['t--REDIRECT---'] = \
            """<meta http-equiv="Refresh" content="0; url='"""+ \
            path+"""'" />"""

    SubCode['t--TITLE---'] = p

    if 'files_dir' in URL_args and len(URL_args['files_dir']) > 0:
        D['files_dir'] = URL_args['files_dir']

    SubCode['t--FILES---'] = tree_.get_tree(D['files_dir'])

    A = {}
    for k in URL_args:
        if k.endswith('_output'):
            k_ = k.replace('_output','')
            A[k_] = URL_args[k]
    zprint(A,'A')
    out = 'k3/__private__/__private3.temp.txt'
    #print('def main(**' in file_to_text(SubCode['---EDITOR---']))
    #if True:#'def main(**' in SubCode['---EDITOR---']:
        #cr(0,r=1)
    if 'run' in A:
        try:
        #cr(1,r=1)
            with open(out, 'w') as f:
                with redirect_stdout(f):
                    if False:#os.path.getmtime(p) > Imports[p+':time']:
                        importlib.reload( Imports[p] )
                        Imports[p+':time'] = time.time()
                    Imports[p].main(**A)
            SubCode['t--OUTPUT---'] += '<hr>'+lines_to_html_str(file_to_text(out))
        except:
            SubCode['t--OUTPUT---'] += \
                '<hr>'+lines_to_html_str("\ncould not run Imports[p].main(**A)")
            cr("could not run Imports[p].main(**A)")

    if 'city_tab' in URL_args:
        SubCode['t--CITY_TAB---'] = """onload="openTab('event', '"""+URL_args['city_tab']+"""')" """
        cr(SubCode['t--CITY_TAB---'])
    else:
        SubCode['t--CITY_TAB---'] = """onload="openTab('event', '-')" """
        cy(SubCode['t--CITY_TAB---'])
    # onload="setURL()"

    return SubCode

#EOF
