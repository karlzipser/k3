
from k3.utils.mini_menu import *





def Navigate_dictionary(Din,A):

    B = {}

    set_Defaults(
        {
            'view':{
                'action':kprint,
                'Args':None,
            },
            'line_print': {
                'action':_line_print,
                #'Args':None,
            },
            'end':{
                'action':None,
                'Args':None,
            },
            'filter':{
                'action':None,
                #'Args':None,      
            },
            'mini_menu':{
                'action':mini_menu,
                'Args':{
                    'B':B,
                    'menu_tuple':(('test',(True,False))),
                },
            }
        },
        A,
    )

    keylist = []


    Commands = {
        'up':['0'],
        'quit':['q'],
        'mini_menu':['m'],
    }

    def nav():
        clear_screen()

        while True:

            lst = go()

            if lst == 'quit':

                if A['end']['action'] is not None:
                    if A['end']['Args'] is None:
                        A['end']['action']()
                    else:
                        A['end']['action'](**A['end']['Args'])

                return

            elif type(lst) == list:

                if 'keylist' in A['view']['Args']:
                    A['view']['Args']['keylist'] = keylist

                if 'D' in A['view']['Args']:
                    A['view']['Args']['D'] = get()

                if A['filter']['action'] is not None:
                    kprint(lst)
                    lst = A['filter']['action'](lst,**A['mini_menu']['Args']['B'])#**A['filter']['Args'])

                A['view']['action'](lst,**A['view']['Args'])   


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

        if r in Commands['quit']:
            return 'quit'

        elif r in Commands['up']:
            up()

        elif r in Commands['mini_menu']:
            B = A['mini_menu']['action'](**A['mini_menu']['Args'])

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
