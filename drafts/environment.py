ENV = namedtuple('_', 'D')({})


def di(path,e=None):
    assert type(path) == str
    kc = path.split('/')
    return da(*kc,e=e)


#,a
Environment = {
    'dictionary': {
        '~':{'a':1}
    },
    'current_prefix_path': '~/',
    'named_paths': {
        'b':{
            'path':'a/',
            'prefix_path':'~/',
        }
    },
    '-p':True,
    '-v':True,
}


def has_form_of_path(s):
    if type(s) == str:
        if len(s) > 1:
            if s[0] != '/':
                if s[-1] == '/':
                    return True
    return False

def has_form_of_named_path(s):
    if type(s) == str:
        if len(s) > 0:
            if '/' not in s:
                return True
    return False    

def is_valid_path(path):
    pass

def get_valid_path(a):
    if has_form_of_path(a):
        return a
    elif has_form_of_named_path:
        D = Environment['named_paths']
        return D[a]['prefix_path'] + D[a]['path']
    else:
        assert False


def o(path_or_name,e=None):

    if has_form_of_named_path(path_or_name):
        path = get_valid_path(path_or_name)
    else:
        path = Environment['current_prefix_path'] + get_valid_path(path_or_name)

    key_list = path[:-1].split('/')
    D = Environment['dictionary']

    if e == None:
        for k in key_list:
            clp('k:',k,'D:',D)#,'D[k]:',D[k])
            D = D[k]
        return D

    else:
        for k in key_list[:-1]:
            clp('k:',k,'D:',D)#,'D[k]:',D[k])
            D = D[k]
        D[key_list[-1]] = e
        return e

#,b
    
def use_keychain(kc,D,num_tuple_to_num=True):
    if num_tuple_to_num:
        kc = _untuple_keychain(kc)   
    for k in kc:
        D = D[k]
    return D


def set_with_keychain(kc,D,e,num_tuple_to_num=True):
    if num_tuple_to_num:
        kc = _untuple_keychain(kc)
    for i in range(len(kc)-1):
        k = kc[i]
        if type(k) is tuple and len(k) == 1:
            k = k[0]
        D = D[k]
    D[kc[-1]] = e

def _untuple_keychain(kc):
    kc_ = []
    for k in kc:
        if type(k) is tuple and len(k) == 1:
            k = k[0]
        kc_.append(k)
    return kc_ 


def da(
        *kc,
        D=ENV.D,
        e=None,
        num_tuple_to_num=True,
    ):
    if e is None:
        return use_keychain(kc,D,num_tuple_to_num)
    else:
        set_with_keychain(kc,D,e,num_tuple_to_num)


