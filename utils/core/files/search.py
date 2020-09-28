from k3.utils.core.files.files import *


os.environ['GLOG_minloglevel'] = '2'

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


def most_recent_file_in_folder(
    path,str_elements=[],
    ignore_str_elements=[],
    return_age_in_seconds=False
):
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

IMAGE_EXTENSIONS = ['jpg','jpeg','JPG','JPEG','png','PNG','tif','tiff','TIF','TIFF']
def get_list_of_image_files_recursively(src):
    lst = []
    for e in IMAGE_EXTENSIONS:
        l = get_list_of_files_recursively2(
            src,
            pattern='*.'+e,
            FILES_ONLY=True
        )
        lst += l
    return lst

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

def main(**A):
    eg(__file__)
    l = get_list_of_files_recursively2(
        opjk(),
        "*.py",
        FILES_ONLY=True,
        DIRS_ONLY=False,
        ignore_underscore=True,
        ignore_Trash=True,
        followlinks=True
    )
    l = sorted(l)
    for m in l:
        print(m)
    

def files_to_dict(path,D={}):
    D['.'] = []
    fs = sggo(path,'*')
    for f in fs:
        if not os.path.isdir(f):
            D['.'].append(fname(f))
        else:
            D[fname(f)] = files_to_dict(f,{})
    return D

    
    
if __name__ == '__main__':
    main()
#EOF
