from k3 import *
ps = ['k3/drafts/sum_.py']
exec(import_str)

_Arguments = a2d("-a 0 -b 0 -m 0 ")


def main(**A):
    
    a=A['a'];b=A['b'];m=A['m']

    O = sum_(a=a,b=b)
    o = O['out']
    o = m * o

    return return_dict(fun_name,o,A,O['str'])

exec(main_str)
#EOF
