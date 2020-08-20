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

R = Record_vars()

CA()
a = 1
b = [2,3,4]


d = loD('data')

l = len(d)
m = zeros((l,l))
P = Percent('x','calculating','calculated')



#R.update()
#kprint(_R.get_new(),'_R')

#R.save()

#sys.exit()


for x in range(l):
    for y in range(l):
        dx = d[x]
        dy = d[y]
        ex = dx['embedding']
        ey = dy['embedding']
        c = sum((ex-ey)**2)
        m[x,y] = c
        if False:
            clf();plt_square()
            plot(ex,ey,'.')
            spause()
        P.show(x,l)
    soD('m',m)
P.show()

s = []
for i in range(l):
    s.append(np.argsort(m[i,:]))


n = 100
for i in range(0,l,10):
    j = s[n][i]
    mi(d[j]['face'],2,img_title=d2s(j,dp(m[n,j]),as_pct(i,l)))
    spause()
    time.sleep(0.2)



#EOF
