# ,a

from k3.utils.misc.dict_access import *


if not interactive() and __name__ == '__main__':


    if '__file__' in locals():
        eg(__file__)

    if False:
        D=files_to_dict(opjh('Desktops_older/Desktop_30Jan19_10h14m01s'),D={})
        D = condense_dict(D)
        oD = dict_access(D,'Desktops_older/Desktop_30Jan19_10h14m01s/')
    D=files_to_dict(opjk(),D={})
    D = condense_dict(D)
    oD = dict_access(D,opjk()+'/')

    #clear_screen()
    oD(up_down='-')
    c = None
    U = {}
    while True:
        c = input('-> ')#_from_choices(choices=['u','d','q','m'])

        if c == 'q':
            break

        if c is None:
            c = '-'

        if c == 'm':
            i = input_int_in_range(
                0,
                10*10,
                d2n('max depth (',D['__meta__']['max_depth'],') >>> ')
            )
            if type(i) is int:
                D['__meta__']['max_depth'] = i

            oD(up_down='-')
            continue
    

        if c in ['u','d']:
            cc = c
        else:
            cc = '-'
        U,print_lines = oD(up_down=cc)

        if str_is_int(c.split(' ')[0]):
            i = int(c.split(' ')[0])
            if i in U:
                p = U[i]['path']
                oD('__meta__/menu_path/',e=p)
                if False:
                    clp(p,'`ybb') #oD('__meta__/menu_path/'),U[i]['path'],p,'`yb')
                    if U[i]['lst_indx'] is None:
                        cy('out:',oD(p))
                    else:
                        cg('out:',oD(p)[U[i]['lst_indx']])
    
            oD(up_down='-')
            if U[i]['lst_indx'] is None:
                cy('out:',oD(p))
            else:
                cg('out:',oD(p)[U[i]['lst_indx']])
            if False:
                if len(c.split(' ')[0]) > 1:
                    if c.split(' ')[1] == 'o':
                        cg('open',
                            opjh('Desktops_older/Desktop_30Jan19_10h14m01s',
                                p),
                            r=1)





#EOF

# ,b



