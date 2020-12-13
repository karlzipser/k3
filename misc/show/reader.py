#!/usr/bin/env python3

"""#,reader.a

python3 k3/misc/show/reader.py 

#,reader.b"""

from k3 import *

Defaults={
    'bucket':opjh('bucket'),
}
A = get_Arguments(Defaults)

M = {
    'src':opjh('iCloud_Links/jpg/2020'),
    'pattern': '*.jpg',
    'max_num_images':randint(16),
    'img_display_list':[],
    'padsize':randint(50),
    'padval':randint(256),
    'extent2': 100,
    'rcratio': 1.5,
}



while True:

    time.sleep(0.001)

    r = mini_menu(M,once=True)

    if r == 'done':
        break

    Bsave(M,'reader')

    try:

        d = Bload('show')
        cm(type(d))
        if d is not None:
            D = d[-1]
            print(fname(D['file']),D['key'])



    
    except KeyboardInterrupt:
        cE('*** KeyboardInterrupt ***')
        sys.exit()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        cE('Exception!',exc_type,file_name,exc_tb.tb_lineno)
        time.sleep(1)
    

