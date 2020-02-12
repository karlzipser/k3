from __future__ import print_function
from __future__ import division

from times import *
from opjs import *

def fname(path):
    return path.split('/')[-1]


def fnamene(path):
    """
    filename, no extension
    """
    return fname(path).split('.')[0]


def pname(path):
    p = path.split('/')[:-1]
    pstr = ""
    for s in p:
        if len(s)>0:
            pstr += '/' + s
    return pstr


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
    return get_files_sorted_by_mtime(a)



def save_obj(obj, name,noisy=True,show_time=False):
    assert_disk_locations([pname(name)])
    if name.endswith('.pkl'):
        name = name[:-len('.pkl')]
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    if noisy:
        timer = Timer()
        a = cf('. . . saved','`',name+'.pkl','`--rb')
        if show_time:
            b = d2s('`','in',dp(timer.time()),'seconds.\r')
        else:
            b=''
        clp(a,b)



def load_obj(name,noisy=True,time=False):
    assert_disk_locations([pname(name)])
    if noisy:
        timer = Timer()
        clp('Loading','`',name,'`--rb','. . .\r'),
    if name.endswith('.pkl'):
        name = name[:-len('.pkl')]
    assert_disk_locations(name+'.pkl')
    with open(name + '.pkl', 'rb') as f:
        o = pickle.load(f)
        if noisy:
            clp(d2s('. . . loaded in',dp(timer.time()),'seconds.\r')),
        return o
        
lo = load_obj

def loD(name,noisy=True):
    return load_obj(opjD(name),noisy)

def so(arg1,arg2,noisy=True):
    try:
        if type(arg1) == str and type(arg2) != str:
            save_obj(arg2,arg1,noisy)
            return
        if type(arg2) == str and type(arg1) != str:
            save_obj(arg1,arg2,noisy)
            return
        if type(arg2) == str and type(arg1) == str:
            pd2s('def so(arg1,arg2): both args cannot be strings')
        assert(False)
    except:
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

def h5r(filename,assert_exists=True):
    if assert_exists:
        assert_disk_locations(filename)
    return h5py.File(filename,'r')
def h5w(filename):
    assert_disk_locations(pname(filename))
    return h5py.File(filename,'w')
def h5rw(filename):
    assert_disk_locations(pname(filename))
    return h5py.File(filename,'r+')



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




#EOF




