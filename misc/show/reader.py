#!/usr/bin/env python3

"""#,reader.a

python3 k3/misc/show/reader.py 

#,reader.b"""

from k3 import *

A = get_Arguments(Defaults={
    'bucket':opjh('bucket'),
})

M = {
    '_max_num_images':10,#IGNORE_INT,
    #'img_display_list':[],
    'padsize':5,#IGNORE_INT,
    'padval':0,#IGNORE_INT,
    'extent2': 500,#IGNORE_INT,
    'rcratio': 1.0,#,IGNORE_FLOAT,
    '_path':opjh('Pictures'),
    '_pattern':'*.jpg',
    'imgs':[],
    '_start':0,
}

_stop = 0

while True:

    time.sleep(0.001)

    prev = (M['_path'],M['_pattern'],M['_start'],_stop)
    r = mini_menu(M,once=True)
    _stop = M['_start']+M['_max_num_images'] 
    if (M['_path'],M['_pattern'],M['_start'],_stop) != prev:
        os_system("""find 'Pictures/17May2013_photos/17May2013_photos' -name "*.JPG" > Desktop/find.temp.274276068.txt""")
        found = find(M['_path'],M['_pattern'],e=1)
        #cm(found,r=0)
        M['imgs'] = sorted_by_cmtime(found)
        #cy(M['imgs'],r=1)
        print(M['_start'],_stop)
        M['imgs'] = M['imgs'][M['_start']:_stop]
        pprint(M['imgs'])
        #raw_enter()

    if r == 'done':
        break

    Bsave(M,'reader')

    try:

        d = Bload('show')
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
    

