#!/usr/bin/env python3

from k3 import *

A = get_Arguments(
    Defaults={
        's':3,
        'r':3,
    }
)

def ke(
    **A,
    ):

    clear_screen()

    for r in range(A['r']):
        for f,m in zip([cg,cr],['GO','STOP']):
            clear_screen()
            for i in range(A['s']):
                f(m+(1+i)*'.') 
                time.sleep(1)


if __name__ == '__main__':

    ke(**A)

#EOF
