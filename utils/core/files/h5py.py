
from k3.utils.core.files.files import *


def h5r(filename,assert_exists=True,use_real_path=False):
    if use_real_path:
        filename = os.path.realpath(filename)
    if assert_exists:
        #cy(filename,ra=1)
        assert_disk_locations(filename)
    return h5py.File(filename,'r')
def h5w(filename,use_real_path=False):
    if use_real_path:
        filename = os.path.realpath(filename)
    assert_disk_locations(pname(filename))
    return h5py.File(filename,'w')
def h5rw(filename,use_real_path=False):
    if use_real_path:
        filename = os.path.realpath(filename)
    assert_disk_locations(pname(filename))
    return h5py.File(filename,'r+')


def save_as_h5py(file_path,D,dtype='float16'):
    F = h5w(file_path)
    clp('writing topics to',file_path)
    for k in D.keys():
        D[k] = na(D[k])
        clp('    ',k,len(D[k]))
        if type(dtype) == dict:
            dt = dtype[k]
        else:
            dt = dtype
        F.create_dataset(k,data=D[k],dtype=dt)
    F.close()
    clp('done.')


def main(**A):
    eg(__file__)
    
if __name__ == '__main__':
    main()



#EOF
