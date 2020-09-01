
#,a

from k3 import *

if False:
    exec(gcsp()) ###############################################


Environment = {

    'create_missing_paths':True,
    'report_implicit_path_creation':True,
    'current_prefix_path': '~/',
    'aliases': {
            'cw':'~/menu/word/current/',
    },
    'messages':[],

    'dictionary': {
        '~':{
            'menu':{
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
                    'current':'---',
                }
            }
        }
    }
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


def pname_(path):
    assert has_form_of_path(path)
    path = path[:-1]
    return pname(path)



def input_int(s='> '):
    c = input(s)
    if str_is_int(c):
        return int(c)
    else:
        return None


def input_int_in_range(a,b,s):
    c = input_int(s)
    if c is None or c < a or c > b:
        return None
    else:
        return c


def select_from_list(lst):
    for i in rlen(lst):
        clp('    ',i,') ',lst[i],s0='')
    i = input_int_in_range(0,len(lst)-1,'>> ')
    return lst[i]




def assert_as(a,s):
    if not a:
        cE(s)

def o(
    p=None,
    e=None,
    w=None,
    s=None,
    u=False,
    d=False,
    a=None,
    message=None,
    ):

    if message:
        Environment['messages'].append( message )

    if u:
        if Environment['current_prefix_path'] == '~/':
            return o(message="already at top")
            ###################
        Environment['current_prefix_path'] = pname_(
            Environment['current_prefix_path']
        ) + '/'
        return o(
            w=Environment['current_prefix_path'],
            message='went up to '+Environment['current_prefix_path']
        )
        ###################

    if d == 1 or d == True or has_form_of_alias(d):
        key_list = Environment['current_prefix_path'][:-1].split('/')
        D = Environment['dictionary']
        for k in key_list:
            k = str_to_tuple_as_necessary(k)
            D = D[k]
        if type(D) == dict:
            if has_form_of_alias(d):
                if d in kys(D):
                    Environment['current_prefix_path'] += d + '/'
                    return o(message=d2s('down to',d))
                    ###################
                else:
                    assert False
            if len(kys(D)) > 1:
                k = select_from_list(kys(D))
            else:
                k = kys(D)[0]
            Environment['current_prefix_path'] += k + '/'
            Environment['messages'].append(d2s('down to',k))
        else:
            Environment['messages'].append("can't go down")
        return o()
        ###################
    elif d == 0 or d == False:
        pass

    else:
        assert False


    if s is None:
        pass
    elif has_form_of_path(s):
        Environment['current_prefix_path'] = s
    else:
        cE("not has_form_of_path(",s,")")


    if w == None:
        prefix = Environment['current_prefix_path']
    else:
        assert_as( has_form_of_path(w) or w == '', d2s("has_form_of_path(",w,") ") )
        prefix = w

    if p is None:
        if w is None:
            p = Environment['current_prefix_path']
            prefix = ''
        else:
            assert has_form_of_path(w)
            p = prefix
            prefix = ''

    if has_form_of_alias(p):
        Environment['messages'].append(d2s("returning from alias",p))
        return o(Environment['aliases'][p],e=e,w='',s=s)
        ###################

    else:
        if not( has_form_of_path(p) ):
            cE("not( has_form_of_path(",p,") )")
        path = prefix + p

    key_list = path[:-1].split('/')
    D = Environment['dictionary']

    if a is not None:
        assert_as(has_form_of_alias(a),"has_form_of_alias(a)")
        Environment['aliases'][a] = path
        Environment['messages'].append(d2s("add alias",a,"to",path))

    if e == None:
        for k in key_list:
            k = str_to_tuple_as_necessary(k)
            assert_as( k in D, d2s("k in D? No,",k,"not in",D))
            D = D[k]
        Environment['messages'].append(d2s("returning value at",path))
        return D
        ###################
    else:
        for k in key_list[:-1]:
            k = str_to_tuple_as_necessary(k)
            if k not in D:
                if Environment['create_missing_paths']:
                    if Environment['report_implicit_path_creation']:
                        Environment['messages'].append( d2s('creating',k) )
                    D[k] = {}
            D = D[k]
        k = str_to_tuple_as_necessary( key_list[-1] )
        D[k] = e
        Environment['messages'].append(d2s("returning value set at",path))
        return e
        ###################

if __name__ == '__main__':



    

    zprint(o(),t='1')

    o('a/b/c/',e=123)

    zprint(o(),t='2')


    o('a/b/d/',e=456)

    zprint(o(),t='3')

    zprint(o(w='~/menu/range/'),t='4')
    #o('b',e=9)

    #zprint(o('~/'))
    #o('cw',e='ted')


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


#,b
    




