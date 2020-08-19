
from k3.utils.mini_menu import *

def EXAMPLE_of_using_Navigate_dictionary():
    pass



def Navigate_dictionary(Din,A):

    set_Defaults(
        {
            'view':{
                'action':kprint,
                'Args':{},
            },
            'line_print': {
                'action':_line_print,
            },
            'end':{
                'action':None,
                'Args':{},
            },
            'filter':{
                'action':None,
                'Args':{},      
            },
            'mini_menu':{
                'action':mini_menu,
                'Args':{
                    'menu_tuple':(('toggle_test',(True,False))),
                },
            },
            'Commands':{
                'up':['0'],
                'quit':['q'],
                'mini_menu':['m'],
            },
        },

        Dst=A,
    )


    A['mini_menu']['Args']['MiniMenu'] = {}
    A['mini_menu']['action'](**A['mini_menu']['Args'])

    keylist = []



    def clear_screen():
        for i in range(5):
            print('\n')

            
    def nav():
        
        clear_screen()

        while True:

            lst = go()

            if lst == 'quit':

                if A['end']['action'] is not None:
                    if len(A['end']['Args']) == 0:
                        A['end']['action']()
                    else:
                        A['end']['action'](Args=A['end']['Args'])

                return

            elif type(lst) == list:

                A['view']['Args']['keylist'] = keylist

                if 'D' in A['view']['Args']:
                    A['view']['Args']['D'] = get()

                if A['filter']['action'] is not None:
                    kprint(lst)
                    lst = A['filter']['action'](lst,Args=A['filter']['Args'],MiniMenu=A['mini_menu']['Args']['MiniMenu'])

                A['view']['action'](lst,Args=A['view']['Args'],MiniMenu=A['mini_menu']['Args']['MiniMenu'])   


    def up():
        if len(keylist) > 0:
            keylist.pop()
        else:
            errPrint('<already at top>')


    def get():
        D = Din
        for k in keylist:
            D = D[k]
        return D




    def listing():

        ctr = 0

        options = []

        D = get()

        if type(D) is list:
            return None,D

        if len(keylist) > 0:
            clp('<up> (0)')

        ks = D.keys()

        for k in ks:
            ctr += 1
            s = d2n('n=',len(D[k]))
            options.append(k)
            A['line_print']['action'](ctr,s,k,D,keylist)

        return options,None


    def go():

        options,action_list = listing()

        if action_list is not None:
            keylist.pop()
            return action_list

        r = raw_input('> ')

        clear_screen()

        if r in A['Commands']['quit']:
            return 'quit'

        elif r in A['Commands']['up']:
            up()

        elif r in A['Commands']['mini_menu']:
            MiniMenu = A['mini_menu']['action'](**A['mini_menu']['Args'])

        elif str_is_int(r):
            if len(options) > 0:
                r_ = int(r)-1
                if r_ < len(options) and r_ >= 0:
                    keylist.append(options[r_])
                else:
                    errPrint(r+' is out of range')
            else:
                errPrint('no options')
        else:
            errPrint('invalid: ' + qtd(r))

    
    return namedtuple('Dnav_object', 'D keylist nav')(Din,keylist,nav)






def _line_print(ctr,s,k,D,keylist):
    if type(D[k]) == dict:
        c = '`wbb'
    else:
        if type(D[k]) == list:
            c = '`bw-'
        else:
            c = '`r'
    clp( '/'.join(keylist+[k]), '`g-b', s, c, d2n('(',ctr,')') )


#EOF
