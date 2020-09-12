# ,a
from k3.utils.collections_.arguments import *
from k3.utils.misc.dict_access import *
from k3.utils.misc.sys import *


Arguments = get_Arguments(
    Defaults={
        'path':'k3',
        'condense_dict':False,
        #'ignore_meta':True,
    }
)


if not interactive() and __name__ == '__main__':


    if '__file__' in locals():
        eg(__file__)

    if False:
        D=files_to_dict(opjh('Desktops_older/Desktop_30Jan19_10h14m01s'),D={})
        D = condense_dict(D)
        oD = dict_access(D,'Desktops_older/Desktop_30Jan19_10h14m01s/')
    name = Arguments['path']#k3'
    D = files_to_dict(opjh(name),D={})
    if Arguments['condense_dict']:
        D = condense_dict(D)
    oD = dict_access(D,name)

    #clear_screen()
    oD(up_down='-')
    c = None
    U = {}


    _re = r'^\s*(\d+)\s*(\w*)$'


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

        m = re.match(_re,c)
        #cg(m.groups())
        if m:
            if str_is_int(m.groups()[0]):
                i = int(m.groups()[0])
                #cb(i)
        #if str_is_int(c.split(' ')[0]):
            #i = int(c.split(' ')[0])
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
                    oDp = oD(p)
                    if type(oDp) is dict:
                        oDp_show = '{...}'
                    elif type(oDp) is list:
                        oDp_show = '[...]'
                    elif type(oDp) is tuple:
                        oDp_show = '(...)'
                    elif type(oDp) is str:
                        oDp_show = oDp
                    else:
                        oDp_show = str(oDp)

                    if U[i]['lst_indx'] is None:
                        out_ = p + oDp_show
                        cy('out:',out_)
                    else:
                        out_ = p+str(oDp[U[i]['lst_indx']])
                        cg('out:',out_)

                    #cm(qtd(m.groups()),r=1)
                    if len(m.groups()[1]) > 0:
                        if m.groups()[1] == 'o':
                    #if len(c.split(' ')) > 1:
                        #cm(0)
                        #if c.split(' ')[1] == 'o':
                            #cm(1,out,type(oDp))
                            if True:#type(oDp) is str:
                                #cm(2)
                                #cb('open',name,out_,r=1)
                                os_system('open',qtd(name+'/'+out_))

                            # o open, e execute, for individual files or for lists of files, c copy to clipboard
                            # 219 o,  219o


#EOF

# ,b



