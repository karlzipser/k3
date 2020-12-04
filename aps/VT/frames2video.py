#!/usr/bin/env python3

from k3.utils import *



H = {
    'direct_Tilden_LCR_12Jul17_09h41m48s_Mr_Yellow/20300_to_-1': [
        #[20499, 21699],
        #[23200, 23533],
        #[24743, 25350],
        #[25591, 25966],
    ],
    'direct_Tilden_LCR_15Jul17_10h52m51s_Mr_Yellow/30000_to_77267' : [
        #[43408, 45231],
        #[46601, 47884],
        #[53399, 57703],
        #[57703, 59103],
        [59182, 60100],
        [61600, 62184],
        [62400, 62916],
        [66800, 67100],
        [68300, 68900],
    ],
}
"""
H = {
    'direct_Tilden_LCR_15Jul17_12h29m14s_Mr_Yellow/16000_to_21117': [
        [16000, 21117],
        #[27909, 32417],
    ],
}
"""
cmd_line = """
python3 k3/aps/VT/recover_driving_map_stuff/trajectory_plotting_example6__mod.py\
    --run RUN\
    --start START\
    --stop STOP\
    --mod 1\
    --future_back_steps 8\
    --use_past False\
    --save_3D_points_in_image True\
    --save_path SAVE\
    --horizon_factor 0.85\
"""

def frames2video(p,a,z,n,d):
    os_system('rm -r Desktop/__temp__; mkdir -p',opjD('__temp__'))
    ctr,missing = 0,0
    for i in range(a,z):
        f = d2p(i,'jpeg')
        #print(opj(p,f))
        ctr += 1
        if len(sggo(opj(p,f))) == 0:
            missing += 1
            print('missing',i)
            continue
        s = d2s('ln -s',opj(p,f),opjD('__temp__',f))
        os_system(s,e=0,a=1)
    print('Missing',missing,'of',ctr,'total.')

    os_system("cd",opjD('__temp__'),"; ffmpeg -i %*.jpeg -pix_fmt yuv420p -r 30 -b:v 14000k",opjD(d,n)+'.mp4')
    os_system('rm -r Desktop/__temp__; mkdir -p',opjD('__temp__'))

if False:
    for rr in H:
        r = pname(rr)
        for s in H[rr]:
            a,z = s[0],s[1]
            p = opj('/Volumes/osx-data/3D_points_in_image_multistep',r)
            n = d2n(pname(r),'-',a,'-',z)
            d = '/Volumes/osx-data/3D_points_in_image_multistep'
            if False:
                frames2video(p,a,z,n,d)
            if True:
                s = cmd_line.replace('START',str(a))
                s = s.replace('STOP',str(z))
                s = s.replace('RUN',r)
                s = s.replace('SAVE',opj('/Volumes/osx-data',r,d2n(a,'-',z)))
            cm(s.replace('--','\n\t--'),r=0)
            os_system(s)

#,a
if True:
    for rr in H:
        r = pname(rr)
        for s in H[rr]:
            a,z = s[0],s[1]
            p = opj('/Volumes/osx-data/',r,d2n(a,'-',z),r,d2n(a,'_to_',z))
            n = d2n(r,'-',a,'-',z)
            d = '/Volumes/osx-data'
            frames2video(p,a,z,n,d)
#,b


























if False:
    if __name__ == '__main__':

        Arguments = get_Arguments({
            ('p','path to frames'):'<none>',
            ('a','start frame'):0,
            ('z','end frame'):-1,
            ('n','video name'):'no_name',
            ('d','destination path'):opjD(),
        })

        for k in Arguments:
            s = d2s(k,'=','Arguments["'+k+'"]')
            if s[0] == '-':
                continue
            exec(s)

        frames2video(p,a,z,n,d)
    #,b

