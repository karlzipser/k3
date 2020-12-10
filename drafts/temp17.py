
if False:
    F = find_files_recursively(opjh('Movies'),'*.mp4',FILES_ONLY=True)
    l = []
    m = []
    if 'o' not in locals():
        o = []
    for p in F['paths']:
        for f in F['paths'][p]:
            #clp(p,'`r--',f,'`g--')
            
            assert (p,f) not in l
            g = opj(F['src'],p,f)
            l.append((p,f))
            if f in m or g in o:
                continue
            else:
                m.append(f)
            
            n = len(sggo(g))
            assert n == 1
            os_system('open',qtd(g))
            os_system(""" osascript -e 'tell application "Terminal" to activate' """,e=0)
            y = raw_enter('1 or 0')
            if y == '1':
                o.append(g)
                cg(o)
if False:
    from pathlib import Path
    symlink = opjD('a.jpg')
    p = Path(symlink).resolve().as_posix()
"""
https://moonbooks.org/Articles/How-to-insert-an-image-a-picture-or-a-photo-in-a-matplotlib-figure/

convert a.jpg -thumbnail '200x200' a.t.gif
"""

# ~ $ find Desktop -type d -name 'IMG_4*' -print > Desktop/__temp.txt__

~ $ find Desktop -type d -regextype sed -regex ".*/[a-z0-9A-Z\-\_]\w\w[0-9]" -print > Desktop/__temp.txt
if False:
    for g in o:
        os_system('open',qtd(g))
        os_system(""" osascript -e 'tell application "Terminal" to activate' """,e=0)
        y = raw_enter('1 or 0')


#,a
def load_caffe_h5py(
    path,
    frames_between_segments=10,
    graphics=False,
    dst=opjD(),
):

    if 'C' not in locals():
        print('loading C...')
        C = h5r(path)
    print(kys(C['segments']['17']))
    ctr = 0
    ks = kys(C['segments'])
    for i in rlen(ks):
        ks[i] = int(ks[i])
    ks = sorted(ks)

    D = {
        'left':[],
        'steer':[],
        'motor':[],
        'state':[],
    }

    for k in ks:#C['segments']:
        cg(k)
        k = str(k)
        imgs = C['segments'][k]['left']

        ctr += shape(imgs)[0]

        if graphics:
            figure(1);clf();plot(C['segments'][k]['steer']);spause()
        for i in range(shape(imgs)[0]):
            for q in kys(D):
                #cb(q)
                if len(shape(C['segments'][k][q][i])) > 0:
                    #cm(k,q,i)
                    img = imgs[i,:,:,:]
                    #mi(img);spause()
                    D[q].append( img )
                else:
                    #cg(k,q,i)
                    dat = C['segments'][k][q][i]
                    #cm(q,i,dat)
                    D[q].append( dat )
            if graphics:
                mci(z55(D['left'][i]),scale=4)
        for i in range(frames_between_segments):
            for q in kys(D):
                D[q].append(0*D[q][-1])

    L = {
        'steer':D['steer'],
        'motor':D['motor'],
        'state':D['state'],
    }
    O = {
        'left_image/vals': D['left'],
    }

    print(ctr,dp(ctr/30/60),'minutes')

    return L,O



path="/Volumes/Tilden/preprocessed_bkp1/caffe_z2/caffe_z2_direct_Tilden_22Dec16_14h13m11s_Mr_Teal.hdf5"
path="/Volumes/Tilden/preprocessed_bkp1/caffe_z2/caffe_z2_direct_Tilden_23Dec16_15h22m12s_Mr_Orange.hdf5"
path="/Volumes/Tilden/preprocessed_bkp1/caffe_z2/caffe_z2_direct_Tilden_22Dec16_14h29m03s_Mr_Teal.hdf5"
path="/Volumes/Tilden/preprocessed_bkp1/caffe_z2/caffe_z2_direct_local_sidewalks_09Oct16_08h30m15s_Mr_Orange.hdf5"
run = fnamene(path)

L,O = load_caffe_h5py(
    path,
    frames_between_segments=10,
    graphics=False,

)

dst=opjD(run)

os_system('mkdir -p',dst)

save_as_h5py(opj(dst,'left_timestamp_metadata.h5py'),L,{'steer':int,'motor':int,'state':int})

save_as_h5py(opj(dst,'original_timestamp_data.h5py'),O,{'left_image/vals':np.uint8})



#,b



#EOF
