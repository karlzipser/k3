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
        if '.meta' not in f and len(sggo(pname(f),'.meta')) == 0:
            jpeg_dirs.append(pname(f))
        else:
            cg('.meta exists for')
    jpeg_dirs = list(set(jpeg_dirs))
    for f in jpeg_dirs:
        cg(f)
        make_thumbs(f)

def get_photo_dirs():
    ff = get_list_of_files_recursively(opjD('Photos'),'*.jpeg',FILES_ONLY=True,ignore_underscore=False)
    photo_dirs = []
    for f in ff:
        if '.meta' not in f:
            photo_dirs.append(pname(f))
    return list(set(photo_dirs))

def verify_meta(p):
    if len(sggo(p,'.meta')) != 1:
        return False,"if len(sggo(p,'.meta')) != 1:"
    if not os.path.isdir(opj(p,'.meta')):
        return False
    if len(sggo(p,'.meta','.meta')) > 0:
        return False,"if len(sggo(p,'.meta','.meta')) > 0:"
    fs = sggo(p,'.meta','*')
    n,d = 0,0
    for f in fs:
        if exname(f) == '.jpeg':
            n += 1
        elif os.path.isdir(f):
            d += 1
    if n and d:
        return False,"if n and d:"
    return True,"Okay"

def verify():
    good = 0
    bad = 0
    p = get_photo_dirs()
    for q in p:
        r,s = verify_meta(q)
        if not r:
            bad += 1
            if s == "if len(sggo(p,'.meta','.meta')) > 0:":
                os_system('rm -r',opj(q,'.meta','.meta'),e=1)
            else:
                cr(q,s,r=1)
                os_system('open',q)
        else:
            good += 1
            cg(q)
    cy('good:',good,'bad:',bad,'total:',good+bad)


def transfer_meta_from_older_version(topic='Photos2020'):

    F = lo(opjh(most_recent_file_in_folder(opj('Logs/kimages',topic))))['full_paths']
    G = {}
    for f in F:
        assert f not in G
        G[fnamene(f)] = F[f]
    ctr = 0
    ff = get_list_of_files_recursively(opjD('Photos'),'*.jpeg',FILES_ONLY=True,ignore_underscore=False)
    for f in ff:
        if '.meta' in f:
            if 'ratings' in f:
                cr(f,'already rated')
                continue
            #if 'ratings' in f:
            #    
            n = f.split('/')[-1].split(' ')[-1].replace('.jpeg','')
            p = pname(f)
            #cg(n,n in G,r=1)
            if n in G:
                l = []
                for a in G[n]:
                    l.append(str(a[0]))
                s = 'ratings=' + ','.join(l) + '|'
                cb(s)
                q = opj(p,s+f.split('/')[-1])
                #os_system('open',pname(f))
                os_system('mv',qtd(f),qtd(q),e=1,a=1,r=0)
                ctr += 1
    cg(ctr,'filenames adjusted,done.')

def open_img_with_Preview(f):
    os_system('open',f)

def quit_Preview():
    os_system(""" osascript -e 'quit app "Preview"' """)
    return
    if False:
        a = unix('ps -ax')
        for b in a:
            if 'Preview.app' in b:
                c = b.split(' ')
                for d in c:
                    if str_is_int(d):
                        os_system('kill',d)
                        return

def rating_from_filename(f):
    
    if 'ratings=' not in f:
        return None

    f = f.split('|')[0]

    f = f.split('ratings=')[-1]

    l = f.split(',')

    c = 0
    
    for a in l:
        
        c += int(a)

    c /= len(l)

    return c



ff = get_photo_dirs()

mm = sggo(f,'.meta','*')
dirs = []
files = []
for m in mm:
    if os.path.isdir(m):
        dirs.append(m)
    else:
        files.append(m)
#EOF

D = {}
years = []
top = opjD('Photos/all')
a = sggo(top,'*')
for b in a:
    years.append(b.split('/')[-1])
for y in years:
    D[y] = {}
for y in years:
    months = []
    c = sggo(top,y,'*')
    for d in c:
        months.append(d.split('/')[-1])
    for m in months:
        D[y][m] = {}
        days = []
        e = sggo(top,y,m,'*')
        for f in e:
            days.append(f.split('/')[-1])
        for g in days:
            h = sggo(top,y,m,g,'.meta/*')
            D[y][m][g] = {}
            D[y][m][g]['<unsorted>'] = []
            for j in h:
                if os.path.isfile(j):
                    D[y][m][g]['<unsorted>'].append(j.split('/')[-1])
                else:
                    D[y][m][g][fname(j)] = []
                    k = sggo(j,'*.jpeg')
                    for u in k:
                        D[y][m][g][fname(j)].append(u.split('/')[-1])
kprint(D)



