
from k3.utils.core import *

def get_Arguments(Defaults={}):
    """
    Examples using get_Arguments:
        python FILE --help
        python FILE --src Desktop/temp.dat
        try using --help
    """#.replace('FILE',__file__)#.replace(opjh(),'')
    def args_to_dictionary(*args):

        for e in args:
            if '--help' in e:
                print_dic_simple(Defaults,'Defaults')
                os.sys.exit()

        if not is_even(len(args[0])):
            print('def args_to_dictionary(*args): Warning, not is_even(len(args[0]))')
            return
        ctr = 0
        keys = []
        values = []
        for e in args[0]:
            if is_even(ctr):
                keys.append(e)
            else:
                values.append(e)
            ctr += 1
        d = {}
        if len(keys) != len(values):
            print("args_to_dictionary(*args)")
            print("given keys are:")
            print(keys)
            print("given values are:")
            print(values)
            raise ValueError('ERROR because: len(keys) != len(values)')
        for k,v in zip(keys,values):
            d[k] = v
        return d

    temp = args_to_dictionary(sys.argv[1:])

    Arguments = {}

    if temp != None:
        Args = {}
        for k in temp.keys():
            Args[k] = temp[k]

        del temp

        

        for a in Args.keys():



            ar = Args[a]

            if a[0] == '-':
                if len(a) == 2:
                    a = a[1]
                    assert(a.islower() or not a.isalpha())
                elif len(a) > 2:
                    a = a[2:]
                else:
                    assert(False)
            else:
                print_dic_simple(Args,'Args')
                cr(
                    '*** Warning, argument',
                    "'"+k+"'",
                    'not proceeded by -- on command line ***',
                    ra=1
                )

            if str_is_int(ar):
                Arguments[a] = int(ar)
            elif str_is_float(ar):
                Arguments[a] = float(ar)
            elif ',' in ar:
                Arguments[a] = ar.split(',')
            elif ar == 'True':
                Arguments[a] = True
            elif ar == 'False':
                Arguments[a] = False        
            else:
                Arguments[a] = ar

    set_Defaults(Defaults,Arguments)

    return Arguments



if __name__ == '__main__':

    clear_screen()
    
    print("""
    Examples using get_Arguments:
        python FILE --help
        python FILE --src Desktop/temp.dat
        try using --help
    """.replace('FILE',__file__).replace(opjh(),''))

    Arguments = get_Arguments(
        Defaults={
            'src':REQUIRED,
            'start_percent':0,
            'end_percent':100,
            'scale_divider':1,
            'save_faces':True,
        }
    )

    print_dic_simple(Arguments,'Arguments')



