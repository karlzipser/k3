


        
from k3.utils.vis.other import *


r = "direct_Tilden_LCR_15Jul17_10h52m51s_Mr_Yellow"
p = opj("/Volumes/Tilden/Tilden/LCR/h5py",r,'original_timestamp_data.h5py')
O = h5r(p)

start,stop = 68300, 68900

fig = figure(1)
h = 94/2
hs = []
for i in range(start,stop,30):
    print(i)
    g = O['left_image']['vals'][i]
    clf()
    mi(g,1)
    plot([0,168],[h,h],'r')
    spause()
    Cdat = Click_Data(FIG=fig,STR='')
    xy_list = Cdat['CLICK'](NUM_PTS=1)
    h = xy_list[0][1]
    hs.append([i,h])
    cg(pct(i-start,stop-start))
    #time.sleep(0.2)
hs=na(hs)
a = hs[-1,1]
hs = list(hs)
hs.append([stop,a])
hs = na(hs)
#soD(d2s(r,'hor'),hs)

from scipy import interpolate
x = hs[:,0]
y = hs[:,1]
f = interpolate.interp1d(x,y)
xnew = np.arange(start,stop+1)
ynew = f(xnew)
soD(d2n(r,'.xy.',start,'_to_',stop),{'x':xnew,'y':ynew})
figure(2);clf()
plot(xnew,ynew,'.')
plot(x,y,'o')
plt.ylim(0,94)




figure(3)
hist(hs[:,1])
plt.xlim(0,94)
spause()


#EOF
