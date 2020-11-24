#!/usr/bin/env python3

from k3 import *

Arguments = get_Arguments(
    Defaults={
        'days':99*365,
        'src':opjh('Library/Mobile Documents/com~apple~CloudDocs'),
        'dst':opjh('iCloud_Links'),
        'descend':True,
        'ignore_underscore':True,
        'do_sys':True
    }
)


def iclnk(
    **A,
    ):

    clear_screen()
    clp(Arguments['src'],'`--rb')
    print('')

    fs = sggo(A['src'],'*')
    for f in fs:
        if A['ignore_underscore'] and fname(f)[0] == '_':
            cg('ignoring',f,'because of underscore.')
            continue
        try:
            isdr = os.path.isdir(f)
            mt = os.path.getmtime(f)
            e = exname(f)
            if e == '':
                e = 'ne'
            if 0 and isdr:
                e = e+'.f'
            if time.time()-A['days']*days < mt:
                dt = datetime.datetime.fromtimestamp(mt)
                path = qtd(d2f('/',A['dst'],'/',e,'/',dt.year,dt.month,dt.day))
                os_system('mkdir -p',path,e=1,a=A['do_sys'])
                os_system('ln -s',qtd(f),path,e=1,a=A['do_sys'])
                if isdr and A['descend']:
                    B = A.copy()
                    B['src'] = f
                    iclnk(**B)
            else:
                cy(fname(f),'is',int((time.time()-mt)/days),'old, not linking.')
        except:
            cr('problem with mtime')
    cy('done.')




if __name__ == '__main__':

    iclnk(**Arguments)

#EOF
