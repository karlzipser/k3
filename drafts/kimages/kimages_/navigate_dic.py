from k3.utils3 import *

if False:
    estr = """file = "/Users/karlzipser/k3/drafts/kimages/kimages_/navigate_dic.py";code=code = file_to_text(file);exec(code);Q = Dnav(D);Q.nav()"""
    Q = Dnav(D); Q.nav(action=open_imgs_with_Preview_action,end_action=quit_Preview,top=top)





def Dnav(Din):
    
    keylist = []


    def nav(action=kprint,end_action=None,**ActionKwargs):
        clear_screen()
        while True:
            w = go()
            if w == 'quit':
                if end_action is not None:
                    end_action()
                return
            elif type(w) == list:
                """
                If current keylist or D needed in call to action functoin,
                include keyword in ActionKwargs with any value (e.g., keylist=None).
                The simple presence of the keyword insures its value will be set below.
                """
                if 'keylist' in ActionKwargs:
                    ActionKwargs['keylist'] = keylist
                if 'D' in ActionKwargs:
                    ActionKwargs['D'] = get()
                action(w,**ActionKwargs)       


    def up():
        if len(keylist) > 0:
            keylist.pop()
        else:
            print('<already at top>')


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

            s = d2n('n=',len(D[k]))
            
            options.append(k)

            if type(D[k]) == dict:
                c = '`wbb'
            else:
                if type(D[k]) == list:
                    c = '`bw-'
                else:
                    c = '`r'

            ctr += 1
            
            clp( '/'.join(keylist+[k]), '`g-b', s, c, d2n('(',ctr,')') )

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

        elif r == 'a':
            lst = []
            E = get()

            for k in E:
                if type(E[k]) == list:
                    lst += E[k]
            return lst

        elif r == '0':
            up()

        elif str_is_int(r):
            if len(options) > 0:
                r_ = int(r)-1
                if r_ < len(options) and r_ >= 0:
                    keylist.append(options[r_])
                else:
                    clp(r,'out of range')
            else:
                cr('no options')
        else:
            print('invalid: ' + r)

    
    return namedtuple('Dnav_object', 'D keylist nav')(D,keylist,nav)



    #EOF
