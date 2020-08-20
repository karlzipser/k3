


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


#EOF
