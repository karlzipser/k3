from k3 import *

_Arguments = a2d(' -a 0 -b 0 ')

def main(**A):
    c = float(A['a']) + float(A['b'])
    return {
        'out':c,
    }
   
   
if __name__ == '__main__':
    zprint( main(**get_Arguments(_Arguments)), t=__file__ )
#EOF
  
