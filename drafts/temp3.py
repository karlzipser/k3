from k3.vis3 import *

CA()

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
P.show()

s = []
for i in range(l):
	s.append(np.argsort(m[i,:]))


n = 20
for i in range(l):
	j = s[n][i]
	mi(d[j]['face'],2,img_title=d2s(j,dp(m[n,j])))
	spause()
	time.sleep(0.2)
