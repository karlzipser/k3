#,a
def files_to_dict(path,D={}):
    D['.'] = []
    fs = sggo(path,'*')
    #cy(fs,r=1)
    for f in fs:
        if not os.path.isdir(f):
            D['.'].append(f)#fname(f))
        else:
            D[fname(f)] = files_to_dict(f,{})
    return D

def files_to_dict2(path,D={},use_fname=False,ignore_underscore=True):
    D['.'] = []

    fs = sggo(path,'*')
    for f in fs:
        #if ignore_underscore:
        #    if fname(f)[0] == '_' and fname(f) != '__init__.py':
        #    continue
        if not os.path.isdir(f):
            if use_fname:
              g = fname(f)
            else:
              g = f
            D['.'].append(g)
        else:
            D[fname(f)] = files_to_dict2(f,{},use_fname,ignore_underscore)
    return D


def files_to_dict_(path):
    D = {'.' : []}
    fs = sggo(path,'*')
    for f in fs:
        if not os.path.isdir(f):
            D['.'].append(f)#fname(f))
        else:
            D[fname(f)] = files_to_dict_(f)
    return D

p = 'k3/utils/core'
D = files_to_dict(opjh(p))
kprint(D)
#,b