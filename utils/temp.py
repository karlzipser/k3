from k3.utils.record_vars import *


if __name__ == '__main__':
    
    clear_screen()

    print('example using Record_vars.\n')

    R = Record_vars(list(globals().keys()),globals())

    if 'e.g. data':
        a = 1
        b = [2,3,4]
        c = {'a':a,'b':b}
        d = [a,b,c]
        P = Percent('P','calculating','calculated')
        P.show(5,10)
        P.show()

    R.save(list(globals().keys()))

    o = loD('D')

    kprint(o,'reloaded R')


#EOF
