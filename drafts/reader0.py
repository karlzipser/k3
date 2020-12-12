#!/usr/bin/env python3

"""#,r0a

python3 k3/drafts/reader0.py \
    --src /Users/karlzipser/Desktop/w1234.txt \
#,r0b"""

from k3 import *

Defaults={
    'src':opjD('w123.txt'),
}
A = get_Arguments(Defaults)

mt = 0

while True:
    try:
        time.sleep(0.01)
        t = os.path.getmtime(A['src'])
        if t > mt:
            mt = t
            txt = file_to_text(A['src'])
            clear_screen()
            print(cf(time_str(mode='Pretty2'),'`--u'),'\n\n',txt)
            if "<QUIT>" in txt:
                break
    except KeyboardInterrupt:
        cE('*** KeyboardInterrupt ***')
        sys.exit()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        cE('Exception!',exc_type,file_name,exc_tb.tb_lineno)
        time.sleep(0.25)
#EOF
