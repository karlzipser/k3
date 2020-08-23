
from k3.utils.collections import *

# minor

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




def make_path_and_touch_file(path):
    os.system('mkdir -p '+pname(path))
    os.system('touch '+path)

def open_run(run_name,h5py_path=None,Runs_dic=None,want_list=['L','O'],verbose=False):
    #cb("run_name =",run_name,"h5py_path =",h5py_path)
    if h5py_path != None:
        path = h5py_path
        #cb("A) path =",path)
    elif Runs_dic != None:
        path = pname(Runs_dic[run_name])
        #cb("B) path =",path)
    else:
        #cb('C)')
        cr("*** Can't open run",run_name,"because h5py_path=None and Runs_dic=None ***")
        return False,False,False
    files = sggo(path,run_name,"*.h5py")
    if len(files) < len(want_list):
        cr("*** Can't open run",run_name,"because len(files) < 3 ***")
        return False,False,False
    Files = {'L':None,'O':None,'F':None,}
    File_names = {'L':'left_timestamp_metadata','O':'original_timestamp_data','F':'flip_images',}
    for n in File_names:
        if n not in want_list:
            continue
        for f in files:
            if File_names[n] in fname(f):
                if verbose:
                    cg('found',f)
                Files[n] = h5r(f)
    for n in Files:
        if Files[n] == None and n in want_list:
            cr("*** Error, lacking",n)
            return False,False,False
    return Files['L'],Files['O'],Files['F']

def open_run2(run_name,Runs_dic=None,want_list=['L','O'],verbose=False):
    h5py_path = find_h5py_path(run_name)
    L,O,F = open_run(run_name,h5py_path=h5py_path,want_list=want_list,verbose=verbose)
    return L,O,F



def try_to_close(lst):
    if type(lst) == str:
        lst = [lst]
    for l in lst:
        try:
            l.close()
            cy('closed')
        except: pass




rd = '\x1b[31m'
gr = '\x1b[32m'
yl = '\x1b[33m'
bl = '\x1b[34m'
mg = '\x1b[35m'
lb = '\x1b[36m'
wh = '\x1b[37m'

wh_bk = '\x1b[40m'
wh_rd = '\x1b[41m'
wh_gr = '\x1b[42m'
wh_bl = '\x1b[44m'
wh_mg = '\x1b[45m'
wh_lb = '\x1b[46m'

mg = '\x1b[35m'
lb = '\x1b[36m'
wh = '\x1b[37m'

og = '\x1b[91m'
underlined = '\x1b[4m'



def find_h5py_path(run_name):
    H = find_files_recursively(opjD('Data'),run_name,DIRS_ONLY=True)
    h5py_path = None
    for p in H['paths']:
        if fname(p) == 'h5py':
            h5py_path = opj(H['src'],p)
            break
    assert h5py_path is not None
    return h5py_path


#EOF
