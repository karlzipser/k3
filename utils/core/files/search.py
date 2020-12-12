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




IMAGE_EXTENSIONS = ['jpg','jpeg','JPG','JPEG','png','PNG','tif','tiff','TIF','TIFF']



def files_to_dict(
    path,
    ignore_underscore=True,
    require_extension=[],
    ignore_extension=['pyc'],
    ignore=[],
    save_stats=False,
    list_symbol='*',
    process_symbol=True,
):
    D = {list_symbol : []}
    fs = sggo(path,'*')
    timer = Timer(0.01)
    for f in fs:
        if timer.check():
            timer.reset()
            #print(time.time())
            print(rndchoice(['/','\\']),end='\r',flush=True)
        if fname(f)[0] == '_' and ignore_underscore:
            continue
        do_continue = False
        for ig in ignore:
            if ig in f:
                do_continue = True
                break
        if do_continue:
            continue
        if not os.path.isdir(f):
            if save_stats:
                f_ = {
                    f:{
                        'mtime':os.path.getctime(f),
                        #'ctime':os.path.getctime(f),
                        'size':os.path.getsize(f),
                    }
                }
            else:
                f_ = f
            if not require_extension or exname(f) in require_extension:
                if not ignore_extension or exname(f) not in ignore_extension:
                    D[list_symbol].append(f_)
        else:
            D[fname(f)] =\
             files_to_dict(
                path=f,
                ignore_underscore=ignore_underscore,
                require_extension=require_extension,
                ignore=ignore,
                save_stats=save_stats,
                )
    return D
    
    


def files_to_list(path,**K):
    return all_values(files_to_dict(path,**K))



def find_list_of_files_recursively(path,pattern,verbose=True):
    F = find_files_recursively(path,pattern,FILES_ONLY=True,verbose=verbose)
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
            if False:#f in m or g in o:
                cm(f,'in m, or',g,'in o')
                continue
            else:
                m.append(f)
            
            n = len(sggo(g))
            assert n == 1
            o.append(g)
    return o


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

if __name__ == '__main__':
    main()
#EOF
