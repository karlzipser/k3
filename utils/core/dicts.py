from k3.utils.core.imports import *


REQUIRED = '__REQUIRED__'

def kys(D):
    return list(sorted(D.keys()))


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

    args_0 = []
    for i in range(len(args[0])):

        if '--' not in args[0][i]:
            if i == 0 or '--' not in args[0][i-1]:
                print("Error with",args[0])
                return

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
    print(o)
    q = o.split('KEYWORD=')
    print(q)
    r = remove_empty(q)
    #print(r)
    #EOF
    U = {}
    print(r)
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
    if U['positional_args'] == True:
        del U['positional_args']

    return U



def get_Arguments(Defaults={},argstr=None):
    """
    Examples using get_Arguments:
        python FILE --help
        python FILE --src Desktop/temp.dat
        try using --help
    """#.replace('FILE',__file__)#.replace(opjh(),'')

    if argstr is None:
        args = ' '.join(sys.argv[1:])
    else:   
        assert type(argstr) is str
        args = argstr
    
    temp = args_to_dict(args)
    
    #temp = args_to_dictionary(arglst) #sys.argv[1:])

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
