
from k3.utils3 import *

def EXAMPLE_of_using_Navigate_dictionary():

    
    Q = {
        1:{
            2:{
                3:[5,6],
                'a':[1,4,3],
            },
            7:{'xx':['a','v','r',[1,2,3]]}
        },
        'qqq':'zzz',
    }

    ND = Navigate_dictionary(Q)

    while True:
        a = raw_input("Enter 'm' or someting else or 'q' to quit $ ")
        if a == 'm':
            ND.nav()
        elif a == 'q':
            return
        else:
            clp(qtd(a),'is not the navigate command.')
    



def Navigate_dictionary(Din):

    Commands = {
        'up':['0'],
        'quit':['q'],
        'mini_menu':['m'],
    }

    keylist = []


    def clear_screen():
        for i in range(5):
            print('\n')

            
    def nav():
        
        clear_screen()

        while True:
            #cm(-1)
            leaf = go()
            cy(leaf)

            if type(leaf) is str and leaf == 'quit':
                #cm(0)
                return None

            elif type(leaf) is not dict:
                cg(leaf)
                #return leaf


    def go():

        options,action_list = listing()

        #cg(options,action_list,keylist)

        if action_list is not None:
            keylist.pop()
            return action_list

        r = raw_input('> ')

        clear_screen()

        if r in Commands['quit']:
            return 'quit'

        elif r in Commands['up']:
            up()

        elif str_is_int(r):
            if len(options) > 0:
                r_ = int(r)-1
                if r_ < len(options) and r_ >= 0:
                    keylist.append(options[r_])
                    return get()
                else:
                    errPrint(r+' is out of range')
            else:
                errPrint('no options')
        else:
            errPrint('invalid: ' + qtd(r))

    
    


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
        keylist_as_strs = []
        for e in keylist:
            keylist_as_strs.append(str(e))

        #clp( '/'.join(keylist_as_strs+[k]), '`g-b', s, c, d2n('(',ctr,')') )
        print( keylist_as_strs+[k], '`g-b', s, c, d2n('(',ctr,')') )


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
            line_print(ctr,s,k,D)

        return options,None


    def _listing():

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
            line_print(ctr,s,k,D)

        return options

    return namedtuple('_', 'D keylist nav')(Din,keylist,nav)



if __name__ == '__main__':
    EXAMPLE_of_using_Navigate_dictionary()

#EOF
