
fs = sggo('/Volumes/Untitled/validation_runs/*')
fs += sggo('/Volumes/Tilden/Tilden/LCR/h5py/*')

for f in fs:
    os_system("ln -s",f,opj('/Users/karlzipser/Desktop/Data/validate_/h5py',fname(f)))


if False:
    args = ' '.join(sys.argv[1:])
    cm(args,r=1)
    if '--run_from_string True' in args:
        cmd_line.replace('--run_from_string True','')
        os_system(cmd_line,e=1,a=1,r=1)
    cm(cmd_line.replace('--','\n--'),r=1)


#, a
from k3.utils.vis.other import *


r = "direct_Tilden_LCR_15Jul17_12h29m14s_Mr_Yellow"
#p = "/Volumes/osx-data/3D_points_in_image_multistep/direct_Tilden_LCR_12Jul17_09h41m48s_Mr_Yellow/20300_to_-1"
p = opj("/Volumes/Tilden/Tilden/LCR/h5py",r,'original_timestamp_data.h5py')
O = h5r(p)

#,a
start = 12000
stop = 19200
fig = figure(1)
h = 94/2
hs = []
for i in range(start,stop,10):
    print(i)
    g = O['left_image']['vals'][i]
    clf()
    mi(g,1)
    plot([0,168],[h,h],'r')
    Cdat = Click_Data(FIG=fig)
    xy_list = Cdat['CLICK'](NUM_PTS=1)
    h = xy_list[0][1]
    hs.append([i,h])
    spause()
    time.sleep(0.2)

#,b

"""
direct_Tilden_LCR_12Jul17_09h41m48s_Mr_Yellow/20300_to_-1
    20499 21699
    23200 23533
    24743 25350
    25591 25966

direct_Tilden_LCR_15Jul17_12h29m14s_Mr_Yellow/30000
43408 45231
46601 47884
53399 57703
57703 59103
59182 60100
61600 62184
62400 62916
66800 67100
68300 68900

"""

('p','path to frames'):'<none>',
('a','start frame'):0,
('z','end frame'):-1,
('n','video name'):'no_name',
('d'),'destination path':opjD(),

#p="/Volumes/osx-data/3D_points_in_image_multistep/direct_Tilden_LCR_15Jul17_10h52m51s_Mr_Yellow/30000_to_77267"
for k in Arguments:
    print(d2s(k,'=','A["',k,'""]'))

os_system('mkdir -p',opj('/Volumes/osx-data','temp'))
for i in range(43408,45231):
    f = d2p(i,'jpeg')
    if len(sggo(opj(p,f))) == 0:
        print('missing',i)
        continue
    s = d2s('ln -s',opj(p,f),opj('/Volumes/osx-data','temp',f))
    os_system(s)
os_system("cd /Volumes/osx-data/temp; ffmpeg -i %*.jpeg -pix_fmt yuv420p -r 30 -b:v 14000k /Volumes/osx-data/temp.mpg")

