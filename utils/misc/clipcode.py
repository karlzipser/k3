from k3.utils.misc.printing import *
from k3.utils.misc.have_using import *

try:
    import pyperclip
except:
    print("Failed: import pyperclip")

def get_code_snippet_(code_file=None,start='#,a',stop='#,b'):
    if code_file is None:
        code_file = most_recent_py_file()
    code_lst = txt_file_to_list_of_strings(code_file)
    snippet_lst = []
    started = False
    for c in code_lst:
        if not started and c == start:
            started = True
        if started and c == stop:
            break
        if started:
            snippet_lst.append(c)
    code_str = '\n'.join(snippet_lst)
    return code_str
gcsp = get_code_snippet_


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

#EOF
