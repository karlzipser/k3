
from k3.utils.core.renaming import *

def opj(*args):
    if len(args) == 0:
        args = ['']
    str_args = []
    for a in args:
        str_args.append(str(a))
    return os.path.join(*str_args)

def opjh(*args):
    return opj(home_path,opj(*args))

def opjD(*args):
    return opjh('Desktop',opj(*args))

def opjk(*args):
    return opjh('k3',opj(*args))

def opjm(*args):
    if not using_osx():
        media_path = opj('/media',username)
        return opj(media_path,opj(*args))
    else:
        media_path = '/Volumes'
        return opj(media_path,opj(*args))

def fname(path):
    return path.split('/')[-1]

def fnamene(path):
    """
    filename, no extension
    """
    return fname(path).split('.')[0]

def exname(path):
    """
    filename, no extension
    """
    try:
        return fname(path).split('.')[1]
    except:
        return ''

def pname(path):
    p = path.split('/')[:-1]
    pstr = ""
    for s in p:
        if len(s)>0:
            pstr += '/' + s
    return pstr

if __name__ == '__main__':
    print(__file__)
    p = opjk('test.py')
    print(p)
    print(fname(p))
    print(fnamene(p))
    print(exname(p))
    print(pname(p))
    print(fname(pname(p)))
#EOF
