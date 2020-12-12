#!/usr/bin/env python3

"""#,r1a

python3 k3/drafts/reader1.py \
    --name a \
#,r1b"""

from k3 import *

Defaults={
    'name':'a',
    'bucket':opjh('bucket'),
    ('timestamp','Put timestamp on every entry'):True,
    'clear_screen':True,
}
A = get_Arguments(Defaults)

"""
def saveDic(D,name,bucket=opjh('bucket'),max_older=3):
    olds = sggo(bucket,d2n(name,'.*'))
    temp = opj(bucket,d2n('----',name,'.',time.time(),'.',random_with_N_digits(9),'.pkl'))
    os_system('mkdir -p',bucket)
    so(D,temp)
    final = opj(bucket,d2n(name,'.',time.time(),'.',random_with_N_digits(9),'.pkl'))
    os_system('mv',temp,final)
    os_system('rm',opj(bucket,d2n('----',name,'.*')))
    for i in range(max(0,(len(olds)-max_older+1))):
        os_system('rm',olds[i],e=1)


_loadDic = {'last_mtime':0}
def loadDic(name,bucket=opjh('bucket')):
    fs = sggo(bucket,name+'*')
    M = {}
    for f in fs:
        M[os.path.getmtime(f)] = f
    new_f = M[sorted(kys(M))[-1]]
    mtime = os.path.getmtime(new_f)
    if mtime <= _loadDic['last_mtime']:
        return None
    else:
        _loadDic['last_mtime'] = mtime
        return lo(new_f)
"""

while True:
    if True:#try:
        time.sleep(0.01)
        D = Bload(A['name'],A['bucket'])
        if D is not None:
            zprint(D)
    """
    except KeyboardInterrupt:
        cE('*** KeyboardInterrupt ***')
        sys.exit()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        cE('Exception!',exc_type,file_name,exc_tb.tb_lineno)
        time.sleep(1)
    """

