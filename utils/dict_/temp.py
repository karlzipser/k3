from k3.utils.dict_.zprint import *

import_str = """
I = {}
exec(get_import_str(ps,I))
fun_name = fnamene(__file__)
"""
main_str = """
if __name__ == '__main__':
    A = get_Arguments(_Arguments)
    R = main(**A)
    zprint(R,t=__file__)
"""

def return_dict(fun_name,out,A,l=[]):
    return {
        'out':out,
        'str':l+[{fun_name:{'in':A,'out':out}}],
    }