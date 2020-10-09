from k3 import *
ps = []
exec(import_str)






def _do(**A):
    a=A['a']; b=A['b']; p=A['p']; 

    c = a + b

    return Out_dict(
        fun_name,
        out=c,
        A=A,
        l=[],
        p=p)
   
_main = _do
_In = a2d('-a 0 -b 0 -p 1')
_Arguments = _In
exec(main_str)
#EOF
  
