#!/usr/bin/env python3

from k3.utils import *

A = get_Arguments({
    ('path', 'path to backup')     : opjh('k3'),
    ('dst', 'where to put backup') : opjh('k3-bkp'),
    ('sec', 'check for backup every --sec sec') : 10,
    ('pat', 'pattern for backup files') : '*.py',
})

def find_list_of_files_recursively(path,pattern):
    F = find_files_recursively(path,pattern,FILES_ONLY=True)
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




times = [0]

while True:
    
    fs = find_list_of_files_recursively(A['path'],A['pat'])

    print(len(fs),'files with pattern',A['pat'],'in',A['path'])

    p = opj(A['dst'],fname(A['path']))

    if times[-1] != 0:
        tstr = '.py  '+time_str('FileSafe',times[-1])
    else:
        tstr = ''

    for f in fs:
        m = os.path.getmtime(f)
        if m > times[-1]:
            d = f.replace(A['path'],p)
            if len(tstr) > 0:
                d = d.replace('.py',tstr+'.py')
                os_system('mkdir -p',pname(d),e=0)
                os_system('cp',f,qtd(d),e=0)
                print('***',d)

    times.append(time.time())

    time.sleep(A['sec'])

#EOF
