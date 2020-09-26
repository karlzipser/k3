from k3.utils.core.imports import *

Arguments = {}

def __print_dic_simple(D,title=''):
    print(title)
    if type(D) is not dict:
        print(D)
    else:
        for k in D:
            print('   ',str(k)+':',str(D[k]))

def print_dic_simple(D,title='',do_print=True,html=False,print_=True):
    el = '\n'
    if html:
        el +=''
    if title != '':
        s = title+el
    else:
        s = ''
    if type(D) is not dict:
        if print_:
            print(D)
    else:
        for k in D:
            s += '   '+str(k)+':'+str(D[k])+el;
    if print_:
        print(s)
    return s

def clear_screen():
    print(chr(27) + "[2J")
    
def eg(file,cs=False):
    if cs:
        clear_screen()
    print('Examples from '+file+':')
    print('') 


def intr(n):
    return np.int(np.round(n))


def qtd(a):
    if a == '':
        return "''"
    if type(a) == str and ((a[0] == '\'' and a[-1] == '\'') or (a[0] == '\"' and a[-1] == '\"')):
        print('*** qtd(): Warning, '+a+' seems to be quoted already ***')
    return '\"'+str(a)+'\"'
    

def raw_enter(optional_str=''):
    return input(optional_str+'   Hit enter to continue > ')


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


def k_in_D(k,D):
    if k not in D:
        return False
    else:
        return D[k]
kin = k_in_D


def is_number(n):
    if type(n) == bool:
        return False
    if type(n) == type(None):
        return False
    return isinstance(n,numbers.Number)


def bound_value(the_value,the_min,the_max):
    if the_value > the_max:
        return the_max
    elif the_value < the_min:
        return the_min
    else:
        return the_value


def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]


def interactive():
    import __main__ as main
    return not hasattr(main, '__file__')
    
def main(**A):
    print("main()")

if __name__ == '__main__':
    eg(__file__)
    main()
    
    
    
    
    
    
    
    
    
    
REQUIRED = '__REQUIRED__'

def kys(D):
    return list(sorted(D.keys()))


def set_Defaults(Defaults,Dst):
    for k in Dst.keys():
        if k not in Defaults.keys():
            print("**** Warning, argument '"+k+"' not in expected Dst:\n\t",list(Defaults.keys()))

    for k in Defaults.keys():
        if k not in Dst.keys():
            if Defaults[k] is REQUIRED:
                print('*** Error. '+qtd('--'+k)+\
                    ' is a required cmd line arg. ***')
                print_dic_simple(Defaults,'Defaults')
                os.sys.exit()
            else:
                Dst[k] = Defaults[k]
    

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




def files_to_dict(path,D={}):
    D['.'] = []

    fs = sggo(path,'*')
    for f in fs:
        if not os.path.isdir(f):
            D['.'].append(fname(f))
        else:
            D[fname(f)] = files_to_dict(f,{})
    return D

    
    
    
    
    
    
    
    

def arg_str_to_args(s):
    r=r'(\S+)\s*'
    return re.findall(r,s)

def args_to_dictionary(*args):

    for e in args:
        if '--help' in e:
            print_dic_simple(Defaults,'Defaults')
            os.sys.exit()

    if False:
        if not is_even(len(args[0])):
            print('def args_to_dictionary(*args): Warning, not is_even(len(args[0]))')
            return

    args_0 = []
    for i in range(len(args[0])):

        if '--' not in args[0][i]:
            if i == 0 or '--' not in args[0][i-1]:
                print("Error with",args[0])
                return

        """
        if '--' in args[0][i] and args[0][i][-2:] == '--':
            args_0.append(args[0][i])
            args_0.append(0)
        """

        if '--' in args[0][i] and args[0][i][:2] == '--':
            args_0.append(args[0][i])
            if i+1 == len(args[0]) or '--' in args[0][i+1] and args[0][i+1][:2] == '--':
                args_0.append(1)
        else:
            args_0.append(args[0][i])



    ctr = 0
    keys = []
    values = []
    for e in args_0:
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


def get_Arguments(Defaults={},argstr=None):
    """
    Examples using get_Arguments:
        python FILE --help
        python FILE --src Desktop/temp.dat
        try using --help
    """#.replace('FILE',__file__)#.replace(opjh(),'')

    if argstr is None:
        arglst = sys.argv[1:]
    else:   
        assert type(argstr) is str
        arglst = arg_str_to_args(argstr)
    
    temp = args_to_dictionary(arglst) #sys.argv[1:])

    Arguments = {}

    if temp != None:
        Args = {}
        for k in temp.keys():
            Args[k] = temp[k]

        del temp

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
                print_dic_simple(Args,'Args')
                print(
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

    set_Defaults(Defaults,Arguments)

    return Arguments

    
#EOF
