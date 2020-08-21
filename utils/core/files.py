
from k3.utils.core.paths import *
from k3.utils.core.times import *
from k3.utils.core.printing import *




os.environ['GLOG_minloglevel'] = '2'

gg = glob.glob
def sgg(d):
    return sorted(gg(d),key=natural_keys)
def sggo(d,*args):
    a = opj(d,*args)
    return sgg(a)
def get_files_sorted_by_mtime(path_specification):
    files = sggo(path_specification)
    Mtimes = {}
    for f in files:
        Mtimes[f] = os.path.getmtime(f)
    return sorted(Mtimes.items(), key=lambda x:x[1])
def tsggo(d,*args):
    a = opj(d,*args)
    #CS_(a)
    return get_files_sorted_by_mtime(a)


def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def dir_as_dic_and_list( path ):
    """Returns a dictionary and list of files and directories within the path.

    Keyword argument:
        path

    Certain types are ignored:
        .*      -- I want to avoid hidden files and directories.
        _*      -- I use underscore to indicate things to ignore.
        Icon*   -- The Icon? files are a nuisance created by
                  Google Drive that I also want to ignore."""
    return_dic = {}
    return_list = []
    for filename in os.listdir(path):
        if not filename[0] == '.': # ignore /., /.., and hidden directories and files
            if not filename[0] == '_': # ignore files starting with '_'
                if not filename[0:4] == 'Icon': # ignore Google Drive Icon things
                    return_dic[filename] = {}
                    return_list.append(filename)
    return_list.sort(key=natural_keys)
    return (return_dic,return_list)




def save_obj(obj, name,noisy=True,show_time=False,use_real_path=False):
    assert_disk_locations([pname(name)])
    name = name.replace('.pkl','')
    if use_real_path:
        name = os.path.realpath(name)
    with open(name + '.pkl', 'wb') as f:
        if use_real_path:
            f = os.path.realpath(f)
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    if noisy:
        timer = Timer()
        a = d2s('. . . saved',name+'.pkl')#,'`--rb')
        if show_time:
            b = d2s('in',dp(timer.time()),'seconds.\r')
        else:
            b=''
        pd2s(a,b)


def load_obj(name,noisy=True,time=False,use_real_path=False):
    assert_disk_locations([pname(name)])
    if noisy:
        timer = Timer()
        pd2s('Loading',name)#,'`--rb','. . .\r'),

    name = name.replace('.pkl','')
    name = name + '.pkl'
    if use_real_path:
        name = os.path.realpath(name)
    assert_disk_locations(name)
    with open(name, 'rb') as f:
        o = pickle.load(f)
        if noisy:
            pd2s(d2s('. . . loaded in',dp(timer.time()),'seconds.\r')),
        return o
        
lo = load_obj

def loD(name,noisy=True,use_real_path=False):
    if use_real_path:
        name = os.path.realpath(name)
    return load_obj(opjD(name),noisy)

def so(arg1,arg2,noisy=True):
    if True:#try:
        if type(arg1) == str and type(arg2) != str:
            save_obj(arg2,arg1,noisy)
            return
        if type(arg2) == str and type(arg1) != str:
            save_obj(arg1,arg2,noisy)
            return
        if type(arg2) == str and type(arg1) == str:
            pd2s('def so(arg1,arg2): both args cannot be strings')
        assert(False)
    else:#except:
        exec(EXCEPT_STR)

def soD(arg1,arg2,noisy=True):
    try:
        if type(arg1) == str and type(arg2) != str:
            save_obj(arg2,opjD(arg1),noisy)
            return
        if type(arg2) == str and type(arg1) != str:
            save_obj(arg1,opjD(arg2),noisy)
            return
        if type(arg2) == str and type(arg1) == str:
            pd2s('def so(arg1,arg2): both args cannot be strings')
        assert(False)
    except:
        exec(EXCEPT_STR)


def txt_file_to_list_of_strings(path_and_filename):
    f = open(path_and_filename,"r") #opens file with name of "test.txt"
    str_lst = []
    for line in f:
        str_lst.append(line.strip('\n'))
    return str_lst

def list_of_strings_to_txt_file(path_and_filename,str_lst,write_mode="w"):
    f = open(path_and_filename,write_mode)
    for s in str_lst:
        f.write(s+'\n')
    f.close()


def text_to_file(f,t):
    list_of_strings_to_txt_file(f,t.split('\n'))


def file_to_text(f):
    return '\n'.join(txt_file_to_list_of_strings(f))




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



def find_files_recursively(
    src,
    pattern,
    FILES_ONLY=False,
    DIRS_ONLY=False,
    ignore_underscore=True,
    ignore_Trash=True,
    followlinks=True,
):
    """
    https://stackoverflow.com/questions/2186525/use-a-glob-to-find-files-recursively-in-python
    """
    files = []
    folders = {}
    ctr = 0
    timer = Timer(5)
    if src[-1] != '/':
        src = src + '/'
    print(d2n('src =' ,src,', pattern = ',"\"",pattern,"\""))
    for root, dirnames, filenames in os.walk(src,followlinks=followlinks):
        assert(not(FILES_ONLY and DIRS_ONLY))
        if FILES_ONLY:
            use_list = filenames
        elif DIRS_ONLY:
            use_list = dirnames
        else:
            use_list = filenames+dirnames
        for filename in fnmatch.filter(use_list, pattern):
            file_ = opj(root,filename)
            folder = pname(file_).replace(src,'')
            if folder not in folders:
                folders[folder] = []
            folders[folder].append(filename)
            ctr += 1
            if timer.check():
                print(d2s(time_str('Pretty'),ctr,'matches'))
                timer.reset()
    if ignore_underscore:
        folders_ = {}
        for f in folders:
            ignore = False
            if ignore_Trash:
                if 'Trash' in f:
                    ignore = True
            g = f.split('/')
            for h in g:
                if len(h) > 0:
                    if h[0] == '_':
                        #cb('ignoring',f)
                        ignore = True
                        break
            if not ignore:
                folders_[f] = folders[f]
        folders = folders_
    data = {}
    data['paths'] = folders
    data['parent_folders'] = [fname(f) for f in folders.keys()]
    data['src'] = src
    data['pattern'] = pattern
    pd2s(ctr,'matches,',len(data['parent_folders']),'parent folders.')
    return data



def get_list_of_files_recursively2(
    src,
    pattern,
    FILES_ONLY=False,
    DIRS_ONLY=False,
    ignore_underscore=True,
    ignore_Trash=True,
    followlinks=True,
):
    files = get_list_of_files_recursively(
        src,
        pattern,
        FILES_ONLY=False,
        DIRS_ONLY=False,
        ignore_underscore=True,
        ignore_Trash=True,
        followlinks=True,
    )
    files2 = []
    for f in files:
        if f[0] == '/':
            f = f[1:]
        files2.append(opj(src,f))
    return files2

def get_list_of_files_recursively(
    src,
    pattern,
    FILES_ONLY=False,
    DIRS_ONLY=False,
    ignore_underscore=True,
    ignore_Trash=True,
    followlinks=True,
):
    D = find_files_recursively(
        src,
        pattern,
        FILES_ONLY=False,
        DIRS_ONLY=False,
        ignore_underscore=True,
        ignore_Trash=True,
        followlinks=True,
    )
    files = []
    for p in D['paths']:
        for f in D['paths'][p]:
            files.append(opj(src,p,f))
    return files




def assert_disk_locations(locations):
    if type(locations) == str:
        locations = [locations]
    for l in locations:
        #cm(d2s("Checking for",l),ra=1)
        if len(gg(l)) < 1:
            if False: # old version
                srpd2s(d2s("Error:\n",l,"not available!"))
                if len(l.split('/')) > 0:
                    spd2s('Could not find',l,'!!!!!!!!!!')
                    raise ValueError(d2s('Could not find',pname(l),'!!!!!!!!!!'))
            #srpd2s(d2s("Error:\n",l,"not available!"))
            #if len(l.split('/')) > 0:
            #   spd2s('Could not find',l,'!!!!!!!!!!')
            raise ValueError(d2s('Could not find',l))
        #assert(False)
        #print(d2s(l,'is there.\n'))





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


def percent_disk_free(disk='/'):
    statvfs = os.statvfs(disk)
    size_of_filesystem_in_bytes = statvfs.f_frsize * statvfs.f_blocks     # Size of filesystem in bytes
    #print statvfs.f_frsize * statvfs.f_bfree      # Actual number of free bytes
    number_of_free_bytes_that_ordinary_users_have = statvfs.f_frsize * statvfs.f_bavail     # Number of free bytes that ordinary users
    percent_free = dp(100*number_of_free_bytes_that_ordinary_users_have/(1.0*size_of_filesystem_in_bytes))
    return percent_free


def find_h5py_path(run_name):
    H = find_files_recursively(opjD('Data'),run_name,DIRS_ONLY=True)
    h5py_path = None
    for p in H['paths']:
        if fname(p) == 'h5py':
            h5py_path = opj(H['src'],p)
            break
    assert h5py_path is not None
    return h5py_path

def stowe_Desktop(dst=False):
    if dst==False:
        dst = opjh('Desktops_older','Desktop_'+time_str())
    print(dst)
    unix('mkdir -p ' + dst)
    _,l = dir_as_dic_and_list(opjD(''))
    for i in l:
        shutil.move(opjD(i),dst)

def stowe_Desktop2(suffix=''):
    if len(suffix) > 0:
        suffix = '__' + suffix
    dst = opjh('Desktops_older','Desktop_'+time_str()+suffix)
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




#EOF
