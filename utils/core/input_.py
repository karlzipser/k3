from k3.utils.core.printing import *

Arguments = {}

def input_int(s='> '):
    c = input(s)
    if str_is_int(c):
        return int(c)
    else:
        return None

def input_from_choices(s='> ',choices=[]):
    c = input(s)
    if str_is_int(c):
        c = int(c)
    if c in choices:
        return c
    else:
        return None

def input_int_in_range(a,b,s):
    c = input_int(s)
    if c is None or c < a or c > b:
        return None
    else:
        return c

def select_from_list(lst,ignore_underscore=False):
    ctr = 0
    #print('aaa',len(lst))
    for i in rlen(lst):
        #print(i)
        if True:#ignore_underscore and lst[i][0] != '_':
            pd2n('    ',i,') ',lst[i])
            ctr += 1
    #print('bbb')
    if ctr > 1:
        i = input_int_in_range(0,len(lst)-1,'>> ')
    else:
        i = 0
    if i is None:
        return None
    return lst[i]

def main(**A):
    print("main()")
    
if __name__ == '__main__':
    eg(__file__)
    main()
#EOF
