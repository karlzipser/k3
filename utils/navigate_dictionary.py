
from k3.utils.mini_menu import *

def Navigate_dictionary(Din,A):
    set_Defaults(
        {
        'view_action':kprint,
        'ViewActionArgs':None,
        'line_print_action':None,
        'LinePrintArgs':None,
        'end_action':None,
        'filter_action':None,
        'FilterArgs':None,       
        },
        A
    )

    keylist = []

    def nav():
        clear_screen()
        if A['line_print_action']==None:
            A['line_print_action'] = line_print
        while True:
            w = go()
            if w == 'quit':
                if A['end_action'] is not None:
                    A['end_action']()
                return
            elif type(w) == list:
                if 'keylist' in A['ViewActionArgs']:
                    A['ViewActionArgs']['keylist'] = keylist
                if 'D' in A['ViewActionArgs']:
                    A['ViewActionArgs']['D'] = get()

                if A['filter_action'] is not None:
                    w = A['filter_action'](w,A['FilterArgs'])

                A['view_action'](w,**A['ViewActionArgs'])       


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

    def line_print(ctr,s,k,D):
        if type(D[k]) == dict:
            c = '`wbb'
        else:
            if type(D[k]) == list:
                c = '`bw-'
            else:
                c = '`r'
        clp( '/'.join(keylist+[k]), '`g-b', s, c, d2n('(',ctr,')') )


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
            A['line_print_action'](ctr,s,k,D)

        return options,None


    def go():

        options,action_list = listing()

        if action_list is not None:
            keylist.pop()
            return action_list

        r = raw_input('> ')

        clear_screen()

        if r == 'q':
            return 'quit'


        elif r == '0':
            up()

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



#EOF
