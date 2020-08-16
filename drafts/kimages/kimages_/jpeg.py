from k3.vis3 import *
import imghdr
import exifread
import magic # pip install python-magic-bin==0.4.14



def metadata(f,show=False):

    #cg(f)

    if show:
        r = get_resized_img(zimread(f),500,500,100,100)
        mci(r)

    I = {
        'file':f,
        'image_type':None,
    }

    try:
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

    except KeyboardInterrupt:
        cr('*** KeyboardInterrupt ***')
        sys.exit()
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



if 'GSP location':

    def _get_if_exist(data, key):
        if key in data:
            return data[key]

        return None


    def _convert_to_degress(value):
        """
        Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
        :param value:
        :type value: exifread.utils.Ratio
        :rtype: float
        """
        d = float(value.values[0].num) / float(value.values[0].den)
        m = float(value.values[1].num) / float(value.values[1].den)
        s = float(value.values[2].num) / float(value.values[2].den)

        return d + (m / 60.0) + (s / 3600.0)
        
    def get_exif_location(exif_data):
        """
        Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)
        based on https://gist.github.com/erans/983821
        """
        lat = None
        lon = None

        gps_latitude = _get_if_exist(exif_data, 'GPS GPSLatitude')
        gps_latitude_ref = _get_if_exist(exif_data, 'GPS GPSLatitudeRef')
        gps_longitude = _get_if_exist(exif_data, 'GPS GPSLongitude')
        gps_longitude_ref = _get_if_exist(exif_data, 'GPS GPSLongitudeRef')

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = _convert_to_degress(gps_latitude)
            if gps_latitude_ref.values[0] != 'N':
                lat = 0 - lat

            lon = _convert_to_degress(gps_longitude)
            if gps_longitude_ref.values[0] != 'E':
                lon = 0 - lon

        return lat, lon



Q = {
    'date':['date_from_exif','date_from_mtime','date_from_ctime'],
    'time':['time_from_exif','time_from_mtime','time_from_ctime'],
    'latitude':['latitude'],
    'longitude':['longitude'],
    'file':['file'],
    'image_type':['image_type'],
    'shape':['shape_from_exif','shape_from_magic','identify'],
    'orientation':['orientation'],
    'file':['file'],
}


def collect_essential_metadata(I):
    U = {}
    for k in Q:
        for i in rlen(Q[k]):
            found = False
            if Q[k][i] in I:
                U[k] = I[Q[k][i]]
                if i > 0:
                    cr('Warning, using',I[Q[k][i]],'which is not first choice.')
                else:
                    pass#cg('Using',Q[k][i],I[Q[k][i]])
                found = True
                break
            if not found:
                cr('Warning,',k,'not found.')
                U[k] = None
    return U

def int_tuple_to_str(a,spacer='-'):
    b = ''
    for i in rlen(a):
        c = a[i]
        d = str(c)
        if c < 10:
            d = '0' + d
        b += d
        if i+1 < len(a):
            b += spacer
    return b


def new_name_dir(U):

    d = int_tuple_to_str(U['date'])

    new_dir = int_tuple_to_str(U['date'],spacer='/')

    t = int_tuple_to_str(U['time'])

    s = int_tuple_to_str(U['shape'],'x')

    lat = str(U['latitude'])
    lon = str(U['longitude'])

    o = str(U['orientation'])

    n = d2s(d,t,lat+','+lon,s,o,fname(U['file']))

    return n,new_dir


#EOF

def make_thumbs(p,s=200):
    fs = sggo(p,'*')
    thumbs_path = opj(p,'.meta')
    os_system('mkdir -p',thumbs_path)
    s = str(s)
    s = s + 'x' + s
    for f in fs:
        os_system('convert',qtd(f),'-resize',s,qtd(opj(thumbs_path,fname(f))),e=1)

def make_all_thumbs():
    ff = get_list_of_files_recursively(opjD('Photos'),'*.jpeg',FILES_ONLY=True,ignore_underscore=False)
    jpeg_dirs = []
    for f in ff:
        if len(sggo(pname(f),'.meta')) == 0:
            jpeg_dirs.append(pname(f))
    jpeg_dirs = list(set(jpeg_dirs))
    for f in jpeg_dirs:
        cg(f)
        make_thumbs(f)


