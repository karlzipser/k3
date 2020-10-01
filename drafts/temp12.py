from k3 import *

_Arguments = {
    'a':0,
    'b':0,
    'pn':False,
}

def main(**A):
    pn = A['pn']
    if pn == 'False':
        pn = False
    if pn: eg(__file__)
    if pn: print_dic_simple(A)
    c = float(A['a']) + float(A['b'])
    if pn: print(c,'\n')
    return c
   
   
if __name__ == '__main__':
    print(" :^)")
    main(**get_Arguments(_Arguments))
#EOF
  
