#!/usr/bin/env python3


"""#,pxa

python3 k3/misc/template_.py -a 10000 -b 10 -t 0.01

#python3 k3/misc/template_.py -a 1000 -b 7 -t 0.3

#,pxb"""



from k3 import *

A = get_Arguments(
    {
        ('a','goal number'):int,
        ('b','step'):1,
        't':0.1,
    }
)

timer = Timer(.5)

def main():
    print('title: test')
    for i in range(0,A['a'],A['b']):
        time.sleep(A['t'])
        percent(i,A['a']-1,timer,title='test loop')
    print('\n')

if __name__ == '__main__':
    main()

#EOF

