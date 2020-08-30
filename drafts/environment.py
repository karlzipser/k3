


#,a

# (1,) -> '1,' and reverse


Environment = {
    'dictionary': {
        '~':{'a':1}
    },
    'current_prefix_path': '~/',
    'named_paths': {
        'renamed_a':{
            'path':'~/a/',
        }
    },
    '-p':True,
    '-v':True,
}

def set_prefix(path):
    Environment['current_prefix_path'] = path


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

def str_to_tuple_as_necessary(s):
    if type(s) == str:
        if len(s) > 1:
            if s[-1] == ',':
                if str_is_int(s[:-1]):
                    return int(s[:-1])
    return s

def o(path_or_name,e=None,w=None,s=None):

    # w is 'with path, temp change'
    # s sets the prefix path

    if has_form_of_named_path(path_or_name):
        path = get_valid_path(path_or_name)
    else:
        path = Environment['current_prefix_path'] + get_valid_path(path_or_name)

    key_list = path[:-1].split('/')
    D = Environment['dictionary']

    if e == None:
        for k in key_list:
            k = str_to_tuple_as_necessary(k)
            clp('k:',k,'D:',D)#,'D[k]:',D[k])
            D = D[k]
        return D

    else:
        for k in key_list[:-1]:
            k = str_to_tuple_as_necessary(k)
            clp('k:',k,'D:',D)#,'D[k]:',D[k])
            D = D[k]
        k = str_to_tuple_as_necessary( key_list[-1] )
        D[k] = e
        return e

#,b
    




