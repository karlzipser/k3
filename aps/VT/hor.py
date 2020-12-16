


        
from k3.utils.vis.other import *


r = "caffe_z2_direct_local_sidewalks_09Oct16_08h30m15s_Mr_Orange"
p = opj("/Volumes/osx-12-5-2020-2TB/temp/h5py",r,'original_timestamp_data.h5py')
O = h5r(p)

start,stop = 2017,3300
start -= 60
stop += 60

fig = figure(1)
h = 94/2
hs = []
for i in range(start,stop,10):
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

"""
/Volumes/osx-12-5-2020-2TB/temp/h5py/caffe_z2_direct_local_sidewalks_09Oct16_08h30m15s_Mr_Orange
2017,3300

/Volumes/osx-12-5-2020-2TB/temp/h5py/caffe_z2_direct_Tilden_23Dec16_15h22m12s_Mr_Orange
4900,5225

/Volumes/osx-12-5-2020-2TB/temp/h5py/caffe_z2_direct_Tilden_22Dec16_14h29m03s_Mr_Teal
20400,21035

/Volumes/osx-12-5-2020-2TB/temp/h5py/caffe_z2_direct_Tilden_23Dec16_15h22m12s_Mr_Orange
1961,2318

/Volumes/osx-12-5-2020-2TB/temp/h5py/caffe_z2_direct_Tilden_23Dec16_15h22m12s_Mr_Orange
9107,9357

/Volumes/osx-12-5-2020-2TB/temp/h5py/caffe_z2_direct_Tilden_23Dec16_15h22m12s_Mr_Orange
329,523

/Volumes/osx-12-5-2020-2TB/temp/h5py/caffe_z2_direct_Tilden_23Dec16_15h22m12s_Mr_Orange
18610,18890

/Volumes/osx-12-5-2020-2TB/temp/h5py/caffe_z2_direct_Tilden_23Dec16_15h22m12s_Mr_Orange
24393,24928
"""
#EOF
