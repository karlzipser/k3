#!/usr/bin/env python3

"""#,key.a

python3 k3/misc/show/key_counter.py 

#,key.b"""

from k3 import *

def _setup_NP():
    _N = {}
    _P = {
        '1':'!',
        '2':'@',
        '3':'#',
        '4':'$',
        '5':'%',
        '6':'^',
        '7':'&',
        '8':'*',
        '9':'(',
        '0':')',
    }
    for k in kys(_P):
        kk = _P[k]
        _N[kk] = k
    from string import ascii_lowercase
    for k in ascii_lowercase:
        #print(k)
        _P[k] = k.upper()
        _N[k.upper()] = k
    return _N,_P

_N,_P = _setup_NP()

def account_for_key(D,c):
    if c not in kys(_P) + kys(_N):
        cE(c,'not in kys(_P) + kys(_N)')
        return
    if c in _P:
        if c not in D:
            D[c] = 0
        D[c] += 1
    elif c in _N:
        if _N[c] in D:
            if D[_N[c]] > 0:
                D[_N[c]] -= 1
                if D[_N[c]] == 0:
                    del D[_N[c]]


def get_key_str(D):
    ks = sorted(kys(D))
    s = []
    for k in ks:
        if str_is_int(k):
            c = ','
        else:
            c = ','
        s.append(d2n(k,c,D[k])+' ')
    s = ''.join(s)
    n = 0
    ctr = 0
    for i in range(10):
        m = str(i)
        if m in D:
            n += D[m] * i
            ctr += D[m]
    if ctr > 0:
        s = s + d2n('avg=',dp(n/ctr))
    if len(s) > 0 and s[-1] == ' ':
        s = s[:-1]
    return s

#EOF
