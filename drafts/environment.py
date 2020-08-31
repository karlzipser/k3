
from k3 import *

#,a

# (1,) -> '1,' and reverse


Environment = {
    'dictionary': {
        '~':{}
    },
    'current_prefix_path': '~/',
    'aliases': {},
    '-p':True,
    '-v':True,
}
Environment = {
    'dictionary': {
        '~':{'menu':{
                'range':{
                    'min':{
                        'current':0,
                    },
                    'max':{
                        'current':10,
                    },
                    '_min':0,
                    '_max':10,
                },
                'set_toggle':False,
                'word': {
                    'current':'adfs',
                    '_options':'adsf',
                },
                'str': {
                    'current':'---'
                }
            }
        }
    },
    'current_prefix_path': '~/',
    'aliases': {
        'cw':'~/menu/word/current/',
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

def has_form_of_alias(s):
    if type(s) == str:
        if len(s) > 0:
            if '/' not in s:
                return True
    return False    



def str_to_tuple_as_necessary(s):
    if type(s) == str:
        if len(s) > 1:
            if s[-1] == ',':
                if str_is_int(s[:-1]):
                    return (int(s[:-1]),)
    return s



def is_valid_path(path):
    try:
        o(path)
        return True
    except:
        return False



def get_valid_path(a):
    if has_form_of_path(a):
        return a
    elif has_form_of_alias:
        D = Environment['aliases']
        return D[a]['prefix_path'] + D[a]['path']
    else:
        assert False





def o(path_or_name=None,e=None,w=None,s=None):

    if has_form_of_path(s):
        Environment['current_prefix_path'] = s

    if w == None:
        prefix = Environment['current_prefix_path']

    else:
        assert w == '' or has_form_of_path(w)
        prefix = w

    if path_or_name is None:
        path_or_name = Environment['current_prefix_path']
        prefix = ''

    if has_form_of_alias(path_or_name):
        #cm(path_or_name,Environment['aliases'][path_or_name])
        return o(Environment['aliases'][path_or_name],e=e,w='',s=s)

    else:
        assert has_form_of_path(path_or_name)
        path = prefix + path_or_name

    key_list = path[:-1].split('/')
    D = Environment['dictionary']

    if e == None:
        for k in key_list:
            k = str_to_tuple_as_necessary(k)
            #cg('k:',k,'D:',D)
            D = D[k]
        return D

    else:
        for k in key_list[:-1]:
            k = str_to_tuple_as_necessary(k)
            #cy('k:',k,'D:',D)
            D = D[k]
        k = str_to_tuple_as_necessary( key_list[-1] )
        D[k] = e
        return e



if __name__ == '__main__':

    clp( o('menu/') )

    #o('a/',e=123)

    zprint(o('menu/'))

    #o('b',e=9)

    #zprint(o('~/'))
    o('cw',e='ted')
#,b
    




