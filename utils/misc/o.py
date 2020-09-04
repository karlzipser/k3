#,a

from k3.utils.misc.zprint import *







def at_least_1_None(*l):
    for q in l:
        if q is None:
            return True
    return False


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


Last_D = [None]

def o(
    p,
    e=None,
    wD=None,
    sD=None,
    create_missing_paths=True,
    report_path_creation=True,
):
    if sD is not None:
        assert wD is None
        Last_D[0] = sD
        D = sD
    elif wD is not None:
        assert sD is None
        D = wD
    else sD is None and wD is None:
        D = Last_D[0]
    assert_as(D is not None,"D is not None")

    assert_as(has_form_of_path(p),d2n('has_form_of_path(',p,')'))

    key_list = p[:-1].split('/')

    if e == None:
        for k in key_list:
            assert_as( k in D, d2s("k in D? No,",k,"not in",D))
            D = D[k]
        return D 
    else:
        for k in key_list[:-1]:
            if k not in D:
                if create_missing_paths:
                    if report_implicit_path_creation:
                        print( d2s('creating',k), W )
                    D[k] = {}
            D = D[k]
        k = key_list[-1]
        D[k] = e
        return e





def _get_path(p,w,s,W):
    prefix = W['current_prefix_path']

    assert_as( at_least_1_None(w,s), "at_least_1_None(w,s)")

    if has_form_of_alias(w):
        w = W['aliases'][w]

    if has_form_of_path(w):
        prefix = w

    if has_form_of_alias(s):
        s = W['aliases'][s]

    if has_form_of_path(s):
        W['current_prefix_path'] = s
        prefix = s

    if has_form_of_alias(p):
        assert_as(s is None, "s is None")
        assert_as(w is None, "w is None")
        path = W['aliases'][p]

    elif has_form_of_path(p):
        path = prefix + p

    elif p is None:
        path = prefix

    else:
        cE(p,'is neither path nor alias')

    return path


def _message(message,W):
    W['messages'] = W['messages'][-W['max_num_messages']:]
    W['message_ctr'] += 1
    W['messages'].append((W['message_ctr'],message))
    


def _up_or_down(u,d,W):
    
    assert_as( at_least_1_None(u,d), "at_least_1_None(u,d)")

    if u == 1:
        if W['current_prefix_path'] == '~/':
            _message("already at top",W)
            return o() ###################
        W['current_prefix_path'] = pname_(
            W['current_prefix_path']
        ) + '/'
        _message('went up to '+W['current_prefix_path'],W)
        return o( w=W['current_prefix_path'] ) ###################

    if d == 1 or d == True or has_form_of_alias(d):
        key_list = W['current_prefix_path'][:-1].split('/')
        D = W['dictionary']
        for k in key_list:
            k = str_to_tuple_as_necessary(k)
            D = D[k]
        if type(D) == dict:
            if has_form_of_alias(d):
                if d in kys(D):
                    W['current_prefix_path'] += d + '/'
                    _message(d2s('down to',d),W)
                    return o() ###################
                else:
                    assert False
            if len(kys(D)) > 1:
                k = select_from_list(kys(D))
            else:
                k = kys(D)[0]
            W['current_prefix_path'] += k + '/'
            _message(d2s('down to',k),W)
        else:
            _message("can't go down",W)
        return o() ###################
    elif d is None:
        pass

    else:
        assert False





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







if __name__ == '__main__':

    if '__file__' in locals(): eg(__file__)

    print(o('a/b/c/',e=1))

    print(o('a/b/d/',e=456,a='d'))

    zprint(o(),t='3')
    
    print(o('a/b/e/',e=789,a='e'))

    zprint(o(),t='4')

    print(o('a/f/g/h/',e=3,a='h'))

    zprint(o(),t='5')

    #print(o(s='~/a/f/'))

    
    #print(o('g/h/',e=6))

    #zprint(o(),t='6')
    
    zprint(World)


if False:
    exec(gcsp()) ###############################################


#EOF





