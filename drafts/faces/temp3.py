from k3.vis3 import *




d = loD('data')

l = len(d)
m = zeros((l,l))
P = Percent('x','calculating','calculated')

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

CA()
n = 386
mi(d[n]['face'],0)
spause()
for i in range(0,l,1):
    j = s[n][i]
    mi(d[j]['face'],1,img_title=d2s(j,dp(m[n,j]),as_pct(i,l)))
    spause()
    time.sleep(0.2)

#EOF
