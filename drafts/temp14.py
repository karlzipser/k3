
def grep(options='',patterns='',files=''):
    s = d2s('grep',options,patterns,files)
    print(s)
    return unix(s)[0]


def make_dummy_rotated2_file(run_path,dummy_src_data):

    L = h5r(opj(run_path,'left_timestamp_metadata.h5py'))
    
    n = len(L['ts'])
    print(n)

    L.close()
    
    D = h5r(dummy_src_data)

    N = {}
    while True:
        for k in D.keys():
            print(k,len(D[k]))
            if k not in N:
                N[k] = D[k][:]
            else:
                N[k] = np.concatenate([N[k],D[k][:]])
        for k in N.keys():
            print(k,shape(N[k]))
        if len(N['turns']) > n:
            break


    for k in N.keys():
        if len(shape(N[k])) == 1:
            N[k] = N[k][:n]
        elif len(shape(N[k])) == 2:
            N[k] = N[k][:n,:]
        elif len(shape(N[k])) == 3:
            N[k] = N[k][:n,:,:]
        else:
            cE(k)
        print(k,shape(N[k]))

    D.close()

    print(fname(run_path))
    save_as_h5py(opjD(fname(run_path)),N)
    return N

N = make_dummy_rotated2_file(
    '/Volumes/Tilden/Tilden/LCR/h5py/direct_Tilden_LCR_12Jul17_09h41m48s_Mr_Yellow',
    'Desktop/Data/_outer_contours/rotated2/tegra-ubuntu_31Oct18_16h06m32s.h5py',
);




