from __future__ import print_function  # print('me') instead of print 'me'
from __future__ import division  # 1/2 == 0.5, not 0

import_list = ['os','os.path','shutil','scipy','scipy.io','string','glob','time','sys','datetime','random','re',
    'subprocess','threading','serial','inspect','fnmatch','h5py','socket','getpass','numbers','math']#,'importlib']
import_from_list = [['FROM','pprint','pprint'],['FROM','termcolor','cprint']]
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



for im in import_list + import_from_list + import_as_list:
    if type(im) == str:
        try:
            exec('import '+im)
            #print("imported "+im)
        except:
            pass
            print('Failed to import '+im)
    else:
        assert(type(im)) == list
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
        unix('nvidia-smi',print_stdout=True)
        time.sleep(t)





#####################################################
#
def get_Arguments():
    def args_to_dictionary(*args):
        if not is_even(len(args[0])):
            print("args_to_dictionary(*args)")
            print("args are:")
            print(args)
            #raise ValueError('ERROR because: not is_even(len(args[0]))')
            spd2s('def args_to_dictionary(*args): Warning, not is_even(len(args[0]))')
            return
        ctr = 0
        keys = []
        values = []
        for e in args[0]:
            if is_even(ctr):
                keys.append(e)
            else:
                values.append(e)
            ctr += 1
        d = {}
        if len(keys) != len(values):
            print("args_to_dictionary(*args)")
            print("given keys are:")
            print(keys)
            print("given values are:")
            print(values)
            raise ValueError('ERROR because: len(keys) != len(values)')
        for k,v in zip(keys,values):
            d[k] = v
        return d

    temp = args_to_dictionary(sys.argv[1:])

    if temp != None:
        Args = {}
        for k in temp.keys():
            Args[k] = temp[k]

        del temp

        Arguments = {}

        for a in Args.keys():
            
            ar = Args[a]

            if a[0] == '-':
                if len(a) == 2:
                    a = a[1]
                    assert(a.islower() or not a.isalpha())
                elif len(a) > 2:
                    a = a[2:]
                else:
                    assert(False)
            else:
                print(Args)
                cr(
                    '*** Warning, argument',
                    "'"+k+"'",
                    'not proceeded by -- on command line ***',
                    ra=1
                )

            if str_is_int(ar):
                Arguments[a] = int(ar)
            elif str_is_float(ar):
                Arguments[a] = float(ar)
            elif ',' in ar:
                Arguments[a] = ar.split(',')
            elif ar == 'True':
                Arguments[a] = True
            elif ar == 'False':
                Arguments[a] = False        
            else:
                Arguments[a] = ar
    return Arguments

if False:
    Arguments = get_Arguments()

#pprint(Arguments)





            

def set_Defaults(Defaults,Dst,required=[]):
    for k in required:
        if k not in Dst:
            cr("*** Error, argument",k,"was required ***",ra=1)
            sys.exit()
    for k in Dst.keys():
        if k not in Defaults.keys() and k not in required:
            cr("**** Warning, argument '"+k+"' not in expected Dst:\n\t",Defaults.keys(),ra=1)
    for k in Defaults.keys():
        if k not in Dst.keys():
            Dst[k] = Defaults[k]

dargs = set_Defaults





    

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







from k3.utils.printing2 import *

identify_file_str = ''

#EOF

