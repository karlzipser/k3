from __future__ import print_function  # print('me') instead of print 'me'
from __future__ import division  # 1/2 == 0.5, not 0

import_list = ['os','os.path','shutil','scipy','scipy.io','string','glob','time','sys','datetime','random','re',
    'subprocess','threading','serial','inspect','fnmatch','h5py','socket','getpass','numbers','math']#,'importlib']
import_from_list = [['FROM','pprint','pprint'],['FROM','termcolor','cprint'],('FROM','collections','namedtuple')]
import_as_list = [['AS','numpy','np']]#,['AS','cPickle','pickle']]



def opj(*args):
    if len(args) == 0:
        args = ['']
    str_args = []
    for a in args:
        str_args.append(str(a))
    return os.path.join(*str_args)
def opjh(*args):
    return opj(home_path,opj(*args))
def opjD(*args):
    return opjh('Desktop',opj(*args))
def opjk(*args):
    return opjh('k3',opj(*args))
def opjm(*args):
    if not using_osx():
        media_path = opj('/media',username)
        return opj(media_path,opj(*args))
    else:
        media_path = '/Volumes'
        return opj(media_path,opj(*args))

def intr(n):
    return np.int(np.round(n))

def as_pct(a,b):
    return d2n(intr(100*a/b),'%')

def qtd(a):
    return '\"'+a+'\"'
    
for im in import_list + import_from_list + import_as_list:
    if type(im) == str:
        try:
            exec('import '+im)
            #print("imported "+im)
        except:
            pass
            print('Failed to import '+im)
    else:
        assert type(im) == list or type(im) == tuple
        if im[0] == 'FROM':
            try:
                exec('from '+im[1]+' import '+im[2])
                # print("from "+im[1]+" imported "+im[2])
            except:
                pass
                print('Failed to from '+im[1]+' import '+im[2])
        else:
            assert(im[0] == 'AS')
            try:
                exec('import '+im[1]+' as '+im[2])
                #print("imported "+im[1]+" as "+im[2])
            except:
                pass
                print('Failed to import '+im[1]+' as '+im[2])           

try:
    import cPickle as pickle
except:
    import pickle

_which_python = sys.version.split(' ')[0]
if _which_python[0] == '3':
    raw_input = input
    using_python3 = True
else:
    using_python3 = False


os.environ['PYTHONUNBUFFERED'] = '1'

rnd = np.random.random
rndint = np.random.randint
rndn = np.random.randn
rndchoice = np.random.choice
na = np.array
host_name = socket.gethostname()
home_path = os.path.expanduser("~")
username = getpass.getuser()
degrees = np.degrees
arange = np.arange
shape = np.shape
randint = np.random.randint
randn = np.random.randn
zeros = np.zeros
ones = np.ones
reshape = np.reshape
mod = np.mod
array = np.array
sqrt = np.sqrt
sin = np.sin
cos = np.cos
sleep = time.sleep

from k3.utils.printing import *
from k3.utils.have_using import *

def k_in_D(k,D):
    if k not in D:
        return False
    else:
        return D[k]


cstr = """
def cQ(*args,**kwargs):
    cprint(d2s_spacer(tuple(list(args)),spacer=' '),'COLOR')
    if k_in_D('ra',kwargs) or k_in_D('r',kwargs):
        cprint('\b  (hit Enter to continue)','COLOR')
        raw_input()
    if k_in_D('t',kwargs):
        time.sleep(kwargs['t'])
"""

for color in ['red','yellow','green','blue','magenta','cyan','white','Grey']:
    an_exec_string = cstr.replace('Q',color[0]).replace('COLOR',color).replace('Grey','grey')
    exec(an_exec_string)

def fname(path):
    return path.split('/')[-1]

def fnamene(path):
    """
    filename, no extension
    """
    return fname(path).split('.')[0]

def exname(path):
    """
    filename, no extension
    """
    try:
        return fname(path).split('.')[1]
    except:
        return ''


def pname(path):
    p = path.split('/')[:-1]
    pstr = ""
    for s in p:
        if len(s)>0:
            pstr += '/' + s
    return pstr


def raw_enter(optional_str=''):
    return raw_input(optional_str+'   Hit enter to continue > ')


def is_even(q):
    if np.mod(q,2) == 0:
        return True
    return False
    

def str_is_int(s):
    try:
        int(s)
        return True
    except:
        return False

def str_is_float(s):
    try:
        float(s)
        return True
    except:
        return False

def rlen(a):
    return range(len(a))


def atoi(text):
    return int(text) if text.isdigit() else text



def dict_to_sorted_list(d):
    l = []
    ks = sorted(d.keys(),key=natural_keys)
    for k in ks:
        l.append(d[k])
    return l
    

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]


def advance(lst,e,min_len=1):
    len_lst = len(lst)
    if len_lst < min_len:
        pass
    elif len_lst > 1.2*min_len:
        lst = lst[-min_len:]
    else:
        lst.pop(0)
    lst.append(e)

def a_key(dic):
    keys = dic.keys()
    k = np.random.randint(len(keys))
    return keys[k]

def an_element(dic):
    return dic[a_key(dic)]

def get_key_sorted_elements_of_dic(d,specific=None):
    ks = sorted(d.keys(),key=natural_keys)
    els = []
    for k in ks:
        if specific == None:
            els.append(d[k])
        else:
            els.append(d[k][specific])
    return ks,els




def nvidia_smi_continuous(t=0.1):
    while True:                                     
        os.system('nvidia-smi')
        time.sleep(t)









    

def get_terminal_size():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows),int(columns)






def getch():
    import sys, termios, tty, os, time
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch








####################################
# exception format:
def et():
    print(
        """
except KeyboardInterrupt:
    cr('\n\n*** KeyboardInterrupt ***\n')
    sys.exit()
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    CS_('Exception!',emphasis=True)
    CS_(d2s(exc_type,file_name,exc_tb.tb_lineno),emphasis=False)        

        """
        )
EXCEPT_STR = """
exc_type, exc_obj, exc_tb = sys.exc_info()
file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
CS_('Exception!',exception=True,newline=False)
CS_(d2s(exc_type,file_name,exc_tb.tb_lineno),emphasis=False)
"""
#
####################################


def os_system(*args,e=0,r=0,a=1):
    s = d2s(*args)
    if(e):
        clp(s,r=r)
    elif r:
        raw_enter()
    if a:
        os.system(s)

def unix(command_line_str, print_stdout=False, print_stderr=False,print_cmd=False):
    command_line_str = command_line_str.replace('~',home_path)
    p = subprocess.Popen(command_line_str.split(), stdout=subprocess.PIPE)
    stdout,stderr = p.communicate()
    if print_cmd:
        print(command_line_str)
    if print_stdout:
        print(stdout)
    if print_stderr:
        print(stderr)
#    return stdout,stderr
    #return stdout.split('\n')
    s = stdout.decode("utf-8")
    return s.split('\n')


def print_dic_simple(D,title=''):
    print(title)
    if type(D) is not dict:
        print(D)
    else:
        for k in D:
            pd2s('   ',k+':',D[k])


REQUIRED = '__REQUIRED__'

def set_Defaults(Defaults,Dst,required=[]):
    for k in required:
        if k not in Dst:
            cr("*** Error, argument",k,"was required ***",ra=1)
            os.sys.exit()
    for k in Dst.keys():
        if k not in Defaults.keys() and k not in required:
            cr("**** Warning, argument '"+k+"' not in expected Dst:\n\t",list(Defaults.keys()),ra=1)

    for k in Defaults.keys():
        if k not in Dst.keys():
            if Defaults[k] is REQUIRED:
                cprint('*** Error. '+qtd('--'+k)+' is a required cmd line arg. ***','white','on_red')
                print_dic_simple(Defaults,'Defaults')
                os.sys.exit()
            else:
                Dst[k] = Defaults[k]



def Percent(title='',prefix='',end_prefix=None):
    D = {
        'first':True,
        'prefix':prefix
    }
    def show(a=None,b=None):
        end = '\r'
        flush = True
        if a is None and b is None:
            a,b = 100,100
            end = '\n'
            flush = False
            if end_prefix is not None:
                D['prefix'] = end_prefix
        if D['first']:
            D['first'] = False
            try:
                clp(title,'`wbb')
            except:
                print(title)
        print(D['prefix']+' '+as_pct(a,b),end=end,flush=flush)
    return namedtuple(
        '_',
        'show')(
        show
    )



#EOF

