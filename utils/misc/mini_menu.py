
from k3.utils.misc.sys import *

def mini_menu(
    MiniMenu={},
    menu_tuple=(),#eg_menu_tuple,
    normal='`--rb',
    emphasis='`--urb',
    err='`wrb',
    cursor='`--rb',
    do_kprint=False,
    tb='\t\t\t',
    pathname=None,
):
    if len(MiniMenu) == 0:
        for c in rlen(menu_tuple):
            MiniMenu[menu_tuple[c][0]] = menu_tuple[c][1][-1]
        cy('initalizing MiniMenu')
        #return

    while True:
        error = False
        clear_screen()
        if do_kprint:
            kprint(MiniMenu)
        if pathname is None:
            p = ''
        else:
            p = d2n('(',pathname.replace(opjh(),''),')')
        clp(tb,'mini-menu:',p,emphasis)
        for c in rlen(menu_tuple):
            clp(tb,str(c)+')',menu_tuple[c][0]+':',MiniMenu[menu_tuple[c][0]],normal)

        input0 = '<None>'
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
                    h = cf(menu_keyword+':')
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
            clp(tb,'Error with entry',qtd(str(input1)),normal,err,r=1)


eg_menu_tuple=(
    ('min',(0,10,0)),
    ('max',(0,10,10)),
    ('show_unrated',(True,False)),
)
    



if __name__ == '__main__':
    
    Arguments = get_Arguments(
        Defaults={
            'path':None,
        }
    )
    kprint(Arguments,'Arguments')

    if type(Arguments['path']) == str:
        os_system('touch',Arguments['path'])
        if len(sggo(Arguments['path'])) == 0:
            cE(Arguments['path'],'is not valid path, setting',"Arguments['path'] = None",r=1)
            Arguments['path'] = None
    try:
        M = lo(Arguments['path'])

    except:
        M = {}


    while True:

        q = input("q-Enter to quit, m-Enter to return to mini_menu  --> ")
        if q == 'q':
            break
        if q != 'm':
            raw_enter('\nYou entered input ('+qtd(q)+') that does nothing.\n')
            print('')
            continue

        mini_menu(
            MiniMenu=M,
            menu_tuple=eg_menu_tuple,
            pathname=Arguments['path']
        )

        kprint(M,'M')

    print('')

    kprint(M,'final M')

    if type(Arguments['path']) == str:
        so(Arguments['path'],M)


#EOF