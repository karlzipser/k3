######
#
ps = ['k3/drafts/temp12.py']
from k3 import *
I = {}
exec(get_import_str(ps,I))
#
######
#
_Arguments = a2d("-a 0 -b 0 -m 0 ")
#
######


def main(a,b,m):
    O = temp12(a=a,b=b)
    o = O['out']
    o = m * o
    return {
        'out':o,
        'str':'',
    }
    
######
#
if __name__ == '__main__':
	A = get_Arguments(_Arguments)
	R = main(**A)
	R['in'] = A
	zprint(R,t=__file__)
#
######EOF

