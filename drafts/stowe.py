from k3 import *

Arguments = get_Arguments(
    Defaults={
        'maxdaysold':7,
        'src':opjD(),
        'multisrc':False,
        'dst':opjh('stowed'),
        'ignore_underscore':True,
    }
)


def stowe(
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
            mt = os.path.getmtime(f)
            if time.time()-A['maxdaysold']*days < mt:
                dt = datetime.datetime.fromtimestamp(mt)
                path = qtd(d2f('/',A['dst'],dt.year,dt.month,dt.day))
                os_system('mkdir -p',path)
                os_system('mv',qtd(f),path,e=1)
            else:
                cy(fname(f),'is',int((time.time()-mt)/days),'old, not stowing.')
        except:
            cr('problem with mtime')
    cy('done.')




if __name__ == '__main__':

    if Arguments['multisrc']:

        ds = sggo(Arguments['src'],'*')

        for d in ds: 
            Arguments['src'] = d 
            stowe(**Arguments)

    else:
        stowe(**Arguments)

#EOF
