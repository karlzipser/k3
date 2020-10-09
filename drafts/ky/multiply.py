from k3 import *
ps = ['k3/drafts/sum_.py']
I = {}
exec(get_import_str(ps,I))
_f = fnamene(__file__)



def _main(**A):
    
    a=A['a'];b=A['b'];m=A['m']

    O = sum_(a=a,b=b,p=1)
    o = O['out']
    o = m * o
    s = ''

    return Out_dict(_f,o,A,O['str'])


_Arguments = a2d("-a 0 -b 0 -m 0 ")



if __name__ == '__main__':
    eg(__file__)
    A = get_Arguments(_Arguments)
    _Out = _main(**A)
    zprint(_Out,t=__file__)

#EOF
