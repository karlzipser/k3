
from k3.utils.strings import *
from k3.utils.array_stuff import *




def mini_menu(
    B,
    tup,
    normal='`---',
    emphasis='`--u',
    err='`wrb',
    cursor='`---',
    do_kprint=True
):
    t = tup
    while True:
        error = False
        clear_screen()
        if do_kprint:
            kprint(B)
        clp('mini-menu:',emphasis)
        for c in rlen(t):
            clp(c,t[c][0],normal)

        s = raw_input(cf('> ',cursor))

        if s == 'q':
            return

        if str_is_int(s):
            n = int(s)
            if n < len(t) and n >= 0:
                u = t[n]
                cb(u[1][0])
                if type(u[1][0]) == type(True):
                    if u[0] not in B:
                        B[u[0]] = True
                    else:
                        B[u[0]] = not B[u[0]]
                else:
                    h = cf(u[0]+':',d2s(*u[1]))
                    v = raw_input(cf(h + ' > ',cursor))

                    if not str_is_float(v):
                        error = True
                        
                    else:
                        if is_number(u[1][0]):
                            if str_is_float(v) and is_number(u[1][0]) and is_number(u[1][1]):
                                if str_is_int(v):
                                    v = int(v)
                                else:
                                    v = float(v)
                                if v >= u[1][0] and v <= u[1][1]:
                                    cm(v)
                                    B[u[0]] = v
                                else:
                                    error = True


                        elif int(v) < len(u[1]) and int(v) >= 0:
                            B[u[0]] = u[1][int(v)]

                        else:
                            error = True
        else:
            error = True

        if error:
            clp('Error with entry',qtd(str(v)),err,r=1)
                    



#EOF