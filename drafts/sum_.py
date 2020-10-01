from k3 import *
ps = []
exec(import_str)


_Arguments = a2d(' -a 0 -b 0 ')



def main(**A):

    a=A['a']; b=A['b']

    c = float(a) + float(b)

    return return_dict(fun_name,c,A)
   

   
exec(main_str)
#EOF
  
