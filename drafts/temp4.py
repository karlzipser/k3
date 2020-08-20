from k3.vis3 import *

def Record_vars():
    
    ls = [list(globals().keys())]

    def update():
        ls.append(list(globals().keys()))
    def get_new():
        N = {}
        for l in ls[-1]:
            if l not in ls[0]:
                if l[0] != '_':
                    g = globals()[l]
                    try:
                        pickle.dumps(g)
                        N[l] = g
                    except:
                        errPrint(d2s('Warning, cannot pickle',qtd(l),'so skipping it.'))
        return N
    def save(f=opjD('D.pkl')):
        update()
        so(get_new(),f)

    return namedtuple(
        '_',
        'update get_new save')(
         update, get_new, save
    )

if __name__ == '__main__':
    
    print('example using Record_vars.\n')
    
    R = Record_vars()

    a = 1
    b = [2,3,4]
    c = {'a':a,'b':b}
    d = [a,b,c]

    P = Percent('x','calculating','calculated')
    P.show(5,10)
    P.show()

    R.save()

    o = loD('D')

    kprint(o,'reloaded R')

#EOF
