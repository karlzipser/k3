from k3.vis3 import *
import imghdr
import exifread


def metadata(f,show=True):

    cg(f)

    if show:
        r = get_resized_img(zimread(f),500,500,100,100)
        mci(r)

    I = {
        'file':f,
        'image_type':None,
    }

    try:
        cb(f,r=1)
        I['image_type'] = imghdr.what(f)
    except:
        cr('imghdr.what failed for',f,r=0)

    try:
        I['magic.from_file'] = magic.from_file(f).replace(' x ','x')
        q = re.search('(\d+)x(\d+)', I['magic.from_file']).groups()
        xy = (int(q[0]),int(q[1]))
        I['shape_from_magic'] = xy
    except:
        cr('magic.from_file failed for',f)

    try:
        I['identify'] = subprocess.check_output(['identify \"'+f+'\"'],shell=True).decode("utf-8")
        q = re.search('(\d+)x(\d+)', I['identify']).groups()
        xy = (int(q[0]),int(q[1]))
        I['shape_from_identify'] = xy
    except:
        cr('identify failed for',f)

    T = {}
    try:
        with open(I['file'], 'rb') as o:
            T = exifread.process_file(o, details=False)

        D = {}
        for k in T:
            D[k] = (T[k].values,T[k].printable)

        w = D['EXIF ExifImageWidth'][0][0]
        l = D['EXIF ExifImageLength'][0][0]
        I['shape_from_exif'] = (w,l)

        I['latitude'],I['longitude'] = get_exif_location(T)

        dt = D['EXIF DateTimeOriginal'][0].split(' ')

        d = dt[0]
        d = d.split(':')
        d = tuple(na(d,int))

        I['date_from_exif'] = d

        d = dt[1]
        d = d.split(':')
        d = tuple(na(d,int))
        I['time_from_exif'] = d

        I['orientation'] = read_orientation(T)
        cb(I['orientation'])
    except:
        cr('exifread failed for',f)

    I['ctime'] = os.path.getctime(f)
    I['mtime'] = os.path.getmtime(f)
    for k in ['ctime','mtime']:
        a = datetime.datetime.fromtimestamp( I[k] )
        I['date_from_'+k] = (a.year,a.month,a.day)
        I['time_from_'+k] = (a.hour,a.minute,a.second)
    
    I['tags'] = T

    return I


def read_orientation(T):
    if "Image Orientation" in T:
        orientation = T["Image Orientation"]
        val = orientation.values
        if 3 in val:
            return 180
        if 6 in val:
            return 270
        if 8 in val:
            return 90
    return 0

