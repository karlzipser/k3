
from k3 import *

raw_code = get_code_snippet_(__file__,start='#,---a',stop='#,---b')

for c in raw_code.split('#.'):
    if not c.isspace():


        cg(qtd(c))
        if '#--' in c:
            c = c.split('#')[0]
            exec("print("+c+")")
        else:
            exec(c)
        #time.sleep(1)


"""
#############################
#,---a
a = 1#.
b = 2#.
a+b #--#.
#.
if True:
    print(a+b)
#.
#,---b
#############################
"""
#EOF





