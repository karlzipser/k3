from k3.utils.core.imports import *

_Arguments = {}

def main(**A):
    eg(__file__)
    print("int(1.9) =",int(1.9))
    print("intr(1.9) =",intr(1.9))
    
    
def bordered(text):
    # https://stackoverflow.com/questions/20756516/python-create-a-text-border-with-dynamic-size
    text = str(text)
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)



def boxed(text,title=''):
    text = str(text)
    lines = text.splitlines()
    width = max(max(len(s) for s in lines),len(title)+1)
    #res = ['┌' + '─' * width + '┐']
    top = '┌' + '─' + title
    top += (width-len(top)+1) * '─' + '┐'
    res = [top]
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)
  
def box(text,title=''):
    print(boxed(text,title))
  
def print_dic_simple(D,title='',html=False,print_=True):
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
    
def eg(f,cs=False):
    if cs:
        clear_screen()
    if False:
        s = "│ Examples from "+f+":"
        print('┌'+(len(s)-1)*'─'+'\n'+s+'\n')
    print(bordered('E.g.s from '+f))



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
    def atoi(text):
        return int(text) if text.isdigit() else text
    return [ atoi(c) for c in re.split('(\d+)', text) ]


def interactive():
    import __main__ as main
    return not hasattr(main, '__file__')
    



def all_values(D):
    def get_all_values(d):
        #https://stackoverflow.com/questions/7002429/how-can-i-extract-all-values-from-a-dictionary-in-python
        if isinstance(d, dict):
            for v in d.values():
                yield from get_all_values(v)
        elif isinstance(d, list):
            for v in d:
                yield from get_all_values(v)
        else:
            yield d
    return sorted(list(get_all_values(D)))




REQUIRED = '__REQUIRED__'

def kys(D):
    return list(D.keys())


def set_Defaults(Defaults,Dst,verbose=False):
    for k in Dst.keys():
        if k not in Defaults.keys():
            if verbose:
                print("*** Warning, argument '"+k+"' not in expected Dst:\n\t",
                    list(Defaults.keys())
                )
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





def remove_empty(l):
    m = []
    for a in l:
        if a != '':
            m.append(a)
    return m

def space(s):
    a = s.split(' ')
    return remove_empty(a)


def args_to_dict(s):
    #print(s)
    m = space(s)
    n = []
    keyword_found = False
    for a in m:
        if not str_is_float(a):
            if a[0] == '-':
                n.append('KEYWORD='+a)
                continue
        if not keyword_found:
            keyword_found = True
            n.insert(0,'KEYWORD=--positional_args')
        n.append(a)
    o = ' '.join(n)
    #print(o)
    q = o.split('KEYWORD=')
    #print(q)
    r = remove_empty(q)
    #print(r)
    #EOF
    U = {}
    #print(r)
    for a in r:
        b = space(a)
        #cg(b)
        c = b[0]
        if len(c) == 2:
            assert c[0] == '-'
            assert c[1].isalpha()
        elif len(c) > 3:
            assert c[0] == '-'
            assert c[1] == '-'
            assert c[2].isalpha()
            for i in range(3,len(c)):
                assert c[i].isalpha() or c[i].isnumeric() or c[i] in ['_','.',',']
        else:
            assert False

        d = b[0].replace('-','')
        if len(b) == 1:
            U[d] = True
        elif len(b) == 2:
            if str_is_int(b[1]):
                U[d] = int(b[1])
            elif str_is_float(b[1]):
                U[d] = float(b[1])
            else:
                U[d] = b[1]
        else:
            U[d] = b[1:]
    if 'positional_args' in U and U['positional_args'] == True:
        del U['positional_args']

    return U

a2d = args_to_dict


def get_Arguments(Defaults={},argstr=None):

    if argstr is None:
        args = ' '.join(sys.argv[1:])
    else:   
        assert type(argstr) is str
        args = argstr
    
    Arguments = args_to_dict(args)

    set_Defaults(Defaults,Arguments)

    return Arguments







########################
#
# relic needed for Learn

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
def parse_to_Arguments(sys_str):
    a = sys_str.split(' ')
    b = []
    for c in a:
        if c != '':
            b.append(c)
    if len(b) > 1:
        b = b[1:]

    temp = args_to_dictionary(b)
    if type(temp) != dict:
        return {}
    #kprint(temp,'temp')
    if temp != None:
        Args = {}
        for k in temp.keys():
            if '/' in temp[k]:
                print('Treating '+temp[k]+' as filename')
                exec("Args[\'"+k+"\'] = '"+temp[k]+"'")
            elif type(temp[k]) == str:
                exec("Args[\'"+k+"\'] = '"+temp[k]+"'")
            else:
                exec('Args[\''+k+'\'] = '+temp[k])
        del temp
        Arguments_ = {}
        for a in Args.keys():
            ar = Args[a]
            if a[0] == '-':
                assert a[0] == '-'
                assert a[1] == '-'
                a = a[2:]
            else:
                print(Args)
                pd2s('\x1b[1m\x1b[41m\x1b[37m',
                    '*** Warning, argument',
                    "'"+k+"'",
                    'not proceeded by -- on command line ***',
                    '\x1b[0m'
                )
                time.sleep(4)
                #raw_enter()
            if str_is_int(ar):
                Arguments_[a] = int(ar)
            elif str_is_float(ar):
                Arguments_[a] = float(ar)
            elif ',' in ar:
                Arguments_[a] = ar.split(',')
            elif ar == 'True':
                Arguments_[a] = True
            elif ar == 'False':
                Arguments_[a] = False        
            else:
                Arguments_[a] = ar
    return Arguments_


def find_files_recursively(
    src,
    pattern,
    FILES_ONLY=False,
    DIRS_ONLY=False,
    ignore_underscore=True,
    ignore_Trash=True,
    followlinks=True,
):
    """
    https://stackoverflow.com/questions/2186525/use-a-glob-to-find-files-recursively-in-python
    """
    files = []
    folders = {}
    ctr = 0
    #timer = Timer(5)
    if src[-1] != '/':
        src = src + '/'
    print('src =' ,src,', pattern = ',"\"",pattern,"\"")
    for root, dirnames, filenames in os.walk(src,followlinks=followlinks):
        assert(not(FILES_ONLY and DIRS_ONLY))
        if FILES_ONLY:
            use_list = filenames
        elif DIRS_ONLY:
            use_list = dirnames
        else:
            use_list = filenames+dirnames
        for filename in fnmatch.filter(use_list, pattern):
            file_ = opj(root,filename)
            folder = pname(file_).replace(src,'')
            if folder not in folders:
                folders[folder] = []
            folders[folder].append(filename)
            ctr += 1
            """
            if timer.check():
                print(d2s(time_str('Pretty'),ctr,'matches'))
                timer.reset()
            """
    if ignore_underscore:
        folders_ = {}
        for f in folders:
            ignore = False
            if ignore_Trash:
                if 'Trash' in f:
                    ignore = True
            g = f.split('/')
            for h in g:
                if len(h) > 0:
                    if h[0] == '_':
                        #cb('ignoring',f)
                        ignore = True
                        break
            if not ignore:
                folders_[f] = folders[f]
        folders = folders_
    data = {}
    data['paths'] = folders
    data['parent_folders'] = [fname(f) for f in folders.keys()]
    data['src'] = src
    data['pattern'] = pattern
    print(ctr,'matches,',len(data['parent_folders']),'parent folders.')
    return data



#
#
############


if __name__ == '__main__':
    main(**_Arguments)

    
#EOF
