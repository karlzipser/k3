

from k3.utils.core import *

REQUIRED = '__REQUIRED__'

def set_Defaults(Defaults,Dst):#,required=[]):
    print_dic_simple(Defaults,'Defaults')
    print_dic_simple(Dst),'Dst'
    for k in Dst.keys():
        if k not in Defaults.keys():
            cr("**** Warning, argument '"+k+"' not in expected Dst:\n\t",list(Defaults.keys()),ra=1)

    for k in Defaults.keys():
        if k not in Dst.keys():
            if Defaults[k] is REQUIRED:
                cprint('*** Error. '+qtd('--'+k)+' is a required cmd line arg. ***','white','on_red')
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




#EOF
