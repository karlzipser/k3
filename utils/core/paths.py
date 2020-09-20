"""
  .
 .
.
"""

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
fn = fname

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
        a = fname(path).split('.')
        if len(a) == 1:
            return ''
        return a[-1]
    except:
        return ''

def pname(path):
    return '/'.join(  path.split('/')[:-1]  )
pn = pname


code = \
"""
p = opjk('test.py')#
p               #
fname(p)        #
fnamene(p)      #
exname(p)       #
fname(p)        #
pname(p)        #
fname(pname(p)) #
"""

def main(**A):
    print("<===> :^)")
    print_dic_simple(A,title='A')
    
    try:
        print(A['arguments'])
        for i in range(int(A['n'])):
            print(i)
    except:
        pass
    a = 0
    for c in code.split('#\n'):
        if c is None or len(c.replace(' ','')) == 0:
            continue
        print("IN["+str(a)+"]: "+c)
        
        if '=' not in c:
            d = "print('      OUT["+str(a)+"]:',"+c+")"
        else:
            d = c
        exec(d)
        print('')
        a += 1

if __name__ == '__main__':
    main()

#EOF
  
  
  
  
  
  
