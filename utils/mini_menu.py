
from k3.utils.strings import *
from k3.utils.array_stuff import *


eg_menu_tuple=(
    ('view',('Preview','kprint')),
    ('min',(0,10)),
    ('max',(0,10)),
    ('show_unrated',(True,False)),
)

def mini_menu(
    MiniMenu={},
    menu_tuple=eg_menu_tuple,
    normal='`---',
    emphasis='`--u',
    err='`wrb',
    cursor='`---',
    do_kprint=False,
    tb='\t\t\t',
    init=False
):
    if init:
    #if len(MiniMenu) == 0:
        for c in rlen(menu_tuple):
            MiniMenu[menu_tuple[c][0]] = menu_tuple[c][1][-1]
        return

    while True:
        error = False
        clear_screen()
        if do_kprint:
            kprint(MiniMenu)
        clp(tb,'mini-menu:',emphasis)
        for c in rlen(menu_tuple):
            clp(tb,str(c)+')',menu_tuple[c][0]+':',MiniMenu[menu_tuple[c][0]],normal)

        input0 = raw_input(cf(tb+' >> ',cursor))

        if input0 == 'q':
            return

        if str_is_int(input0):
            n = int(input0)
            if n < len(menu_tuple) and n >= 0:
                menu_row = menu_tuple[n]
                menu_keyword = menu_row[0]
                menu_choices = menu_row[1]
                if type(menu_choices[0]) == type(True):
                    if menu_keyword not in MiniMenu:
                        MiniMenu[menu_keyword] = True
                    else:
                        MiniMenu[menu_keyword] = not MiniMenu[menu_keyword]
                else:
                    h = cf(menu_keyword+':')#,d2s(*menu_choices[:-2]))
                    input1 = raw_input(cf(tb + h + ' >>> ',cursor))

                    if not str_is_float(input1):
                        error = True
                        
                    else:
                        if is_number(menu_choices[0]):
                            if str_is_float(input1) and is_number(menu_choices[0]) and is_number(menu_choices[1]):
                                if str_is_int(input1):
                                    input1 = int(input1)
                                else:
                                    input1 = float(input1)
                                if input1 >= menu_choices[0] and input1 <= menu_choices[1]:
                                    cm(input1)
                                    MiniMenu[menu_keyword] = input1
                                else:
                                    error = True


                        elif int(input1) < len(menu_choices) and int(input1) >= 0:
                            MiniMenu[menu_keyword] = menu_choices[int(input1)]

                        else:
                            error = True
        else:
            error = True

        if error:
            clp(tb,'Error with entry',qtd(str(input1)),err,r=1)
                    



#EOF