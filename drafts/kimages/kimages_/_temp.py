from k3.vis3 import *
import imghdr
import exifread

def get_args():
    
    import argparse

    par = argparse.ArgumentParser(
        prog=__file__,
        description='.....',
        fromfile_prefix_chars='@',
        add_help=True,
    ); aa = par.add_argument


    aa(
        '--file',
        action='store',
        type=str,
        required=True,
        help='file',
    )

    return par.parse_args()

args = get_args()


# pip install python-magic-bin==0.4.14
from k3.vis3 import *
import imghdr
import magic

if True:
    import exifread 
    
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


#,a
import k3.drafts.kimages.kimages_.jpeg as jpeg
Is = {}
ff=sggo("Pictures/Photos Library.photoslibrary/originals/A/*.jpeg")
#ff = sggo("Pictures/heic_to_jpeg/*.jpeg")
for f in ff:

    try:
        q = imghdr.what(f)
    except:
        q = None
        cr('imghdr.what failed for',f,r=0)

    if q == 'jpeg':
        Is[f] = jpeg.metadata(f)

#,b
#EOF
