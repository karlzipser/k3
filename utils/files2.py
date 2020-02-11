from __future__ import print_function
from __future__ import division

from files import *

def most_recent_file_in_folder(path,str_elements=[],ignore_str_elements=[],return_age_in_seconds=False):
    files = gg(opj(path,'*'))
    if len(files) == 0:
        return None
    candidates = []
    for f in files:
        fn = fname(f)
        is_candidate = True
        for s in str_elements:
            if s not in fn:
                is_candidate = False
                break
        for s in ignore_str_elements:
            if s in fn:
                is_candidate = False
                break
        if is_candidate:
            candidates.append(f)
    mtimes = {}
    if len(candidates) == 0:
        return None
    for c in candidates:
        mtimes[os.path.getmtime(c)] = c
    mt = sorted(mtimes.keys())[-1]
    c = mtimes[mt]
    if return_age_in_seconds:
        return c,time.time()-mt
    else:
        return c




def assert_disk_locations(locations):
    if type(locations) == str:
        locations = [locations]
    for l in locations:
        if len(gg(l)) < 1:
            raise ValueError(d2s('Could not find',l))




def try_to_close(lst):
    if type(lst) == str:
        lst = [lst]
    for l in lst:
        try:
            l.close()
            cy('closed')
        except: pass



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




def percent_disk_free(disk='/'):
    statvfs = os.statvfs(disk)
    size_of_filesystem_in_bytes = statvfs.f_frsize * statvfs.f_blocks     # Size of filesystem in bytes
    number_of_free_bytes_that_ordinary_users_have = statvfs.f_frsize * statvfs.f_bavail     # Number of free bytes that ordinary users
    percent_free = dp(100*number_of_free_bytes_that_ordinary_users_have/(1.0*size_of_filesystem_in_bytes))
    return percent_free



def stowe_Desktop(dst=False):
    if dst==False:
        dst = opjh('Desktops_older','Desktop_'+time_str())
    print(dst)
    unix('mkdir -p ' + dst)
    _,l = dir_as_dic_and_list(opjD(''))
    for i in l:
        shutil.move(opjD(i),dst)

def restore_Desktop(src):
    _,l = dir_as_dic_and_list(opjD(''))
    if len(l) > 0:
        print('**** Cannot restore Desktop because Desktop is not empty.')
        return False
    _,l = dir_as_dic_and_list(src)
    for i in l:
        shutil.move(opjh(src,i),opjD(''))






def sort_dir_by_ctime(dir_path):
    """
    https://www.w3resource.com/python-exercises/python-basic-exercise-71.php
    """
    from stat import S_ISREG, ST_MTIME, ST_MODE
    import os, sys, time
    data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
    data = ((os.stat(path), path) for path in data)
    # regular files, insert creation date
    data = ((stat[ST_MTIME], path)
               for stat, path in data if S_ISREG(stat[ST_MODE]))
    paths = []
    for cdate, path in sorted(data):
        paths.append(path)
    return paths



def project_path__to__project_import_prefix(project_path):
    project_path = project_path.replace(opjh(),'')
    a = project_path.split('/')
    c = []
    for b in a:
        if len(b) > 0:
            c.append(b)
    project_import_prefix = '.'.join(c)
    return project_import_prefix



def file_modified_test(path,mtime_prev):
    mtime = os.path.getmtime(path)
    if mtime > mtime_prev:
        return mtime
    else:
        return 0

#EOF




