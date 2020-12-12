#!/usr/bin/env python3

"""#,r1a

python3 k3/drafts/reader1.py \
    --name a \
#,r1b"""

from k3 import *

Defaults={
    'name':'a',
    'bucket':opjh('bucket'),
}
A = get_Arguments(Defaults)


while True:
    if True:#try:
        time.sleep(0.001)
        d = Bload(A['name'],A['bucket'])
        if d is not None:
            #zprint(D)
            D = d[-1]
            print(fname(D['file']),D['key'])
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

