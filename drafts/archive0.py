#!/usr/bin/env python3

"""#,arca
python3 k3/drafts/archive0.py
#,arcb"""

from k3 import *
from pathlib import Path


Arguments = get_Arguments(
    Defaults={
        'src':opjD(),
        'dst':opjh('Archived'),
        'cp' : True,
        'ignore_underscore':True,
    }
)


def file_type(f):
    e = exname(f)
    e = e.lower()
    Q = {
        'jpg':'jpg',
        'jpeg':'jpg',
        'png':'png',
        'tiff':'tiff',
        'gif':'gif',
        'pdf':'pdf',
        'rtf':'rtf',
        'txt':'txt',
    }
    if e in Q:
        return Q[e]
    else:
        return 'unknown'


#,a

to_ignore = ["Downloads","Documents","Library",".Trash",]
to_ignore += ["kzpy3","k3","k3-bkp","Stowed",]



def source_file_is_okay(symlink):
    if os.path.exists(symlink) == True:
        if os.path.isdir(symlink) == False:
            if os.path.islink(symlink) == True:
                if os.path.getsize(symlink) > 0:
                    return True
    return False



def update_link(
    symlink,
    to_ignore=to_ignore,
    verbose=True,
):
    source_file = Path(symlink).resolve().as_posix()

    id_folder_name = fname(pname(source_file))

    if source_file_is_okay(symlink):
        if verbose:
            cg('source_file_is_okay')
        return True
    else:
        ignore_str = ''
        for i in range(len(to_ignore)-1):
            ignore_str = ignore_str + d2s(' -path',opjh(to_ignore[i]),'-o ')
        ignore_str = ignore_str + d2s(' -path',opjh(to_ignore[-1]))
        cg("Using unix find command to locate archived files")
        unix_str = "find "+opjh()[:-1]+" -type d ( " + ignore_str + " ) -prune -false -o -name *_t=*"
        print(unix_str)
        find_list = unix( unix_str )
        for f in find_list:
            cg(f,id_folder_name)
            if fname(f) == id_folder_name:
                os_system('rm',qtd(symlink),e=1)
                os_system('ln -s',qtd(opj(f,fname(source_file))),qtd(symlink),e=1)
                assert source_file_is_okay(symlink)
                return True
    return False

#,b
#"Archived/pall/jpg/2020/10/5/10E68917-4BF3-4FEA-91B5-D195989B2A54 copy.jpeg  _t=1601920090.6705475/10E68917-4BF3-4FEA-91B5-D195989B2A54 copy.jpeg" =="Archived/pall/jpg/2020/10/5/10E68917-4BF3-4FEA-91B5-D195989B2A54 copy.jpeg  _t=1601920090.6705475/10E68917-4BF3-4FEA-91B5-D195989B2A54 copy.jpeg"

def archive(A):

    fs = sggo(A['src'],'*')

    for f in fs:

        if A['ignore_underscore'] and fname(f)[0] == '_':
            cb('ignoring',f,'because of underscore.')
            continue

        if os.path.islink(f):
            cb('ignoring',f,'because it is link.')
            continue

        if os.path.isdir(f):
            cb('ignoring',f,'because it is a directory.')
            continue

        mt = os.path.getmtime(f)
        dt = datetime.datetime.fromtimestamp(mt)

        idnum = d2n(mt)

        if False:
            path = opj(
                A['dst'],
                file_type(f),
                dt.year,
                dt.month,
                dt.day,
                d2n(fname(f),'  ',idnum),
            )

        ft = file_type(f)
        dst = A['dst']
        ft = file_type(f)
        year = dt.year
        month = dt.month
        day = dt.day
        fname_ = fname(f)

        path = opj(dst,'all',ft,year,month,day,d2n(fname_,'  _t=',idnum))
        #dlinks = opj(dst,ft,year,month,day,'_links')
        #mlinks = opj(dst,ft,year,month,'_links')
        #ylinks = opj(dst,ft,year,'_links')
        new_f = opj(path,fname_)



        os_system('mkdir -p',qtd(path),e=1)
        #os_system('mkdir -p',qtd(dlinks),e=1)
        #os_system('mkdir -p',qtd(mlinks),e=1)
        #os_system('mkdir -p',qtd(ylinks),e=1)

        if A['cp']:
            op = 'cp'
        else:
            op = 'mv'

        os_system(op,qtd(f),qtd(path),e=1)

        for wh,fn in (('400x400','_preview.jpg'),('100x100','_thumbnail.gif')):
            os_system(
                'convert',qtd(new_f),
                "-thumbnail "+wh,
                qtd(opj(path,fn)),
                e=1)

        #for lnk in [dlinks,mlinks,ylinks]:
        #    os_system('ln -ignore_str',qtd(new_f),qtd(opj(lnk,fname_)),e=1)


    cy('done.')


def assert_link_is_valid(f):
    if len(sggo(f)) == 1:
        return True
    else:
        return False

#def assert_archive_link_is_valid(f):

if __name__ == '__main__':

    archive(Arguments)

#EOF
