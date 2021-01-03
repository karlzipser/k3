#!/usr/bin/env python3

from k3.utils import *

record_PID(__file__,just_one=True)


A = get_Arguments(
    {
        ('path', 'path to backup')     : opjh('k3'),
        ('dst', 'where to put backup') : opjh('k3-bkp'),
        ('sec', 'check for backup every --sec sec') : 10,
        ('pat', 'pattern for backup files') : '*.py',
        'verbose':False,
    },
    verbose=True,
    file=__file__,
)

#print_dic_simple(A,title=__file__)

times = [0]

while True:
    
    fs = find_list_of_files_recursively(A['path'],A['pat'],verbose=A['verbose'])

    if A['verbose']:
        cb(len(fs),'files with pattern',A['pat'],'in',A['path'])

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
                clp('***',d,'`wbb')

    times.append(time.time())

    time.sleep(A['sec'])

#EOF

