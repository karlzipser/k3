
from k3.utils.misc.printing import *
from k3.utils.misc.have_using import *

try:
    import pyperclip
except:
    print("Failed: import pyperclip")

def get_code_snippet_():
    code_file = most_recent_py_file()
    code_lst = txt_file_to_list_of_strings(code_file)
    snippet_lst = []
    started = False
    for c in code_lst:
        if not started and c == '#,a':
            started = True
        if started and c == '#,b':
            break
        if started:
            snippet_lst.append(c)

    code_str = '\n'.join(snippet_lst)
    return code_str
gcsp = get_code_snippet_

def get_code_snippet():
    code_str = get_code_snippet_()
    if using_osx():
        setClipboardData(code_str)
    else:
        pyperclip.copy(code_str)
    try:
        clp('set clipboard from','`',
            cf(pname(code_file)+'/','`--d',fname(code_file),'`--b',s1=''),
            cf('(',len(snippet_lst),' lines)','`y-d',s0='')
        )
    except:
        clp('set clipboard from',pname(code_file)+'/',fname(code_file),'(',len(snippet_lst),' lines)')
        
    if len(snippet_lst) == 0:
        clp('*** No code snippet. Did you use #,a and #,b ? ***','`rwb')


gsp = get_code_snippet

def most_recent_py_file(path=opjk(),return_mtime=False):
    max_mtime = 0
    for dirname,subdirs,files in os.walk(path):
        for fname in files:
            if len(fname) >= 3:
                if fname[-3:] == '.py':
                    full_path = os.path.join(dirname,fname)
                    mtime = os.stat(full_path).st_mtime
                    if mtime > max_mtime:
                        max_mtime = mtime
                        max_dir = dirname
                        max_file = fname
    if return_mtime:
        return opj(max_dir,max_file),max_mtime
    else:
        return opj(max_dir,max_file)


def getClipboardData():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    if type(data) != str:
        data = data.decode("utf-8")
    return data
gcd = getClipboardData
def setClipboardData(data):
    """
    setClipboardData
    """
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    try:
        p.stdin.write(data)
    except:
        p.stdin.write(bytes(data,'utf-8'))
    p.stdin.close()
    retcode = p.wait()
scd = setClipboardData

   
#,a
if __name__ == '__main__':
    


    code = """
clear_screen()
if '__file__' in locals(): eg(__file__)
clp('most_recent_py_file:', most_recent_py_file())
print('')
c = getClipboardData()
print("getClipboardData()")
print('')
clp(c,'`m--')
    """
    for c in code.split('\n'):
        if not c.isspace():
            clp(c,'`--u')
            exec(c)
"""
print('')
print("gsp()")
print('')
gsp()
print('')
print("getClipboardData()")
print('')
c = getClipboardData()
print('')
clp(c,'`m--')
print('')
"""
#,b
#EOF
