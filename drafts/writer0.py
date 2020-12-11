#!/usr/bin/env python3

"""#,w0a

python3 k3/drafts/writer0.py \
    --dst /Users/karlzipser/Desktop/w1234.txt \
    --write_mode a \
    --start_empty False \

#,w0b"""

from k3 import *

Defaults={
    'dst':opjD('w123.txt'),
    'write_mode':'a',
    'start_empty':False,
}
A = get_Arguments(Defaults)

mt = 0
if  A['start_empty']:
    print('start_empty')
    os_system('rm',A['dst'])

while True:
    try:
        text_to_file(A['dst'],d2s(time.time()),write_mode=A['write_mode'])
        time.sleep(1)

    except KeyboardInterrupt:
        cE('*** KeyboardInterrupt ***')
        text_to_file(A['dst'],"<QUIT>"+'\n',write_mode="a")
        sys.exit()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        cE('Exception!',exc_type,file_name,exc_tb.tb_lineno)
        time.sleep(0.25)
#EOF
