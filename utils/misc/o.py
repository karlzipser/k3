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
    elif sD is None and wD is None:
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
                    if report_path_creation:
                        print( d2s('creating',k) )
                    D[k] = {}
            D = D[k]
        k = key_list[-1]
        D[k] = e
        return e





if __name__ == '__main__':

    o('a/b/c/d/e/',e=1,sD={})
    Q = o('a/b/c/e/')
    o('a/b/c/e/',e=o('a/',wD=Q))#a/b/c/d/'))
    #o('a/b/c/e/f/',2)

    zprint(Last_D[0])
#,b

if False:
    exec(gcsp()) ###############################################


#EOF





