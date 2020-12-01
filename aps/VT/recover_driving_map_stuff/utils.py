from k3 import *


def vec(heading,encoder,motor,sample_frequency=30.,vel_encoding_coeficient=1.0/2.6): #2.3): #3.33
    velocity = encoder * vel_encoding_coeficient # rough guess
    if motor < 49:
        velocity *= -1.0
    a = [0,1]
    a = array(rotatePoint([0,0],a,heading))
    a *= velocity/sample_frequency
    return array(a)

def double_interp_1D_array(a):
    b = []
    for i in range(len(a)-1):
        c = a[i]
        d = a[i+1]
        e = (c+d)/2.0
        b.append(c)
        b.append(e)
    b.append(a[-1])
    return na(b)

def double_interp_2D_array(a):
    b = double_interp_1D_array(a[:,0])
    c = double_interp_1D_array(a[:,1])
    d = zeros((len(b),2))
    d[:,0] = b
    d[:,1] = c
    return d




def f___(x,A,B):
    return A*x+B

def find_h5py_path(run_name):
    H = find_files_recursively(opjD('Data'),run_name,DIRS_ONLY=True)
    h5py_path = None
    for p in H['paths']:
        if fname(p) == 'h5py':
            h5py_path = opj(H['src'],p)
            break
    assert h5py_path is not None
    return h5py_path

def make_path_and_touch_file(path):
    os.system('mkdir -p '+pname(path))
    os.system('touch '+path)




def open_run(run_name,h5py_path=None,Runs_dic=None,want_list=['L','O'],verbose=False):
    #cb("run_name =",run_name,"h5py_path =",h5py_path)
    if h5py_path != None:
        path = h5py_path
        #cb("A) path =",path)
    elif Runs_dic != None:
        path = pname(Runs_dic[run_name])
        #cb("B) path =",path)
    else:
        #cb('C)')
        cr("*** Can't open run",run_name,"because h5py_path=None and Runs_dic=None ***")
        return False,False,False
    files = sggo(path,run_name,"*.h5py")
    if len(files) < len(want_list):
        cr("*** Can't open run",run_name,"because len(files) < 3 ***")
        return False,False,False
    Files = {'L':None,'O':None,'F':None,}
    File_names = {'L':'left_timestamp_metadata','O':'original_timestamp_data','F':'flip_images',}
    for n in File_names:
        if n not in want_list:
            continue
        for f in files:
            if File_names[n] in fname(f):
                if verbose:
                    cg('found',f)
                Files[n] = h5r(f)
    for n in Files:
        if Files[n] == None and n in want_list:
            cr("*** Error, lacking",n)
            return False,False,False
    return Files['L'],Files['O'],Files['F']


def open_run2(run_name,Runs_dic=None,want_list=['L','O'],verbose=False):
    h5py_path = find_h5py_path(run_name)
    L,O,F = open_run(run_name,h5py_path=h5py_path,want_list=want_list,verbose=verbose)
    return L,O,F




if 'from vis3':

    import warnings
    warnings.filterwarnings("ignore")
    from scipy.optimize import curve_fit

    def rotatePoint(centerPoint,point,angle):
        """http://stackoverflow.com/questions/20023209/function-for-rotating-2d-objects
        Rotates a point around another centerPoint. Angle is in degrees.
        Rotation is counter-clockwise"""
        angle = math.radians(angle)
        temp_point = point[0]-centerPoint[0] , point[1]-centerPoint[1]
        temp_point = ( temp_point[0]*math.cos(angle)-temp_point[1]*math.sin(angle) , temp_point[0]*math.sin(angle)+temp_point[1]*math.cos(angle))
        temp_point = temp_point[0]+centerPoint[0] , temp_point[1]+centerPoint[1]
        return temp_point


    def rotatePolygon(polygon,theta):
        """http://stackoverflow.com/questions/20023209/function-for-rotating-2d-objects
        Rotates the given polygon which consists of corners represented as (x,y),
        around the ORIGIN, clock-wise, theta degrees"""
        theta = math.radians(theta)
        rotatedPolygon = []
        for corner in polygon :
            rotatedPolygon.append(( corner[0]*math.cos(theta)-corner[1]*math.sin(theta) , corner[0]*math.sin(theta)+corner[1]*math.cos(theta)) )
        return na(rotatedPolygon)

    def corrected_angle(slope,point,origin):
        alpha = angle_clockwise((1,0),(1,slope))

        x = point[0]-origin[0]
        y = point[1]-origin[1]

        if x >= 0 and y >= 0:
            alpha = 360 - alpha
        elif x < 0 and y >= 0:
            alpha = 180 - alpha
        elif x < 0 and y < 0:
            alpha = 180+360 - alpha
        elif x >= 0 and y < 0:
            alpha = 90-alpha+270
        else:
            assert False

        return alpha

    def angle_clockwise(A, B):
        inner=inner_angle(A,B)
        det = determinant(A,B)
        if det<0: #this is a property of the det. If the det < 0 then B is clockwise of A
            return inner
        else: # if the det > 0 then A is immediately clockwise of B
            return 360-inner

    def inner_angle(v,w):
       cosx=dot_product(v,w)/(length(v)*length(w))
       if cosx > 1.0:
            cosx = 1.0
       elif cosx < -1.0:
            cosx = -1.0
       rad=acos(cosx) # in radians
       return rad*180/pi # returns degrees

    from math import acos
    from math import sqrt
    from math import pi

    def length(v):
        return math.sqrt(v[0]**2+v[1]**2)
    def dot_product(v,w):
       return v[0]*w[0]+v[1]*w[1]
    def determinant(v,w):
       return v[0]*w[1]-v[1]*w[0]



if 'vector functions':


    def vec(heading,encoder,motor,sample_frequency=30.,vel_encoding_coeficient=1.0/2.6): #2.3): #3.33
        velocity = encoder * vel_encoding_coeficient # rough guess
        if motor < 49:
            velocity *= -1.0
        a = [0,1]
        a = array(rotatePoint([0,0],a,heading))
        a *= velocity/sample_frequency
        return array(a)


    def line_function(x,A,B):
        return A*x+B


    def get_alpha(xy):
        if type(xy) == list or type(xy) == tuple:
            xy = na(xy)
        m,b = curve_fit(line_function,xy[:,0],xy[:,1])[0]
        alpha = corrected_angle(m,xy[-1,:],xy[0,:])
        return alpha


    def rotate_alpha(alpha,xy):
        xy_rotated = rotatePolygon( xy, alpha)
        return xy_rotated


    def magnitude(a):
        return np.sqrt(a[0]**2+a[1]**2)


    def dist(A,B):
        return np.sqrt( (A[0]-B[0])**2 + (A[1]-B[1])**2 )


    def distance_decimate_vector(v,d):
        ref = v[0,:]
        u = [ref]
        for i in range(0,len(v)-1):
            e = dist(v[i],v[i+1])
            if dist(ref,v[i]) >= d:
                ref = v[i]
                u.append(ref)
        u.append(v[-1])
        return na(u)



if '3d functions':

    def double_interp_1D_array(a):
        b = []
        for i in range(len(a)-1):
            c = a[i]
            d = a[i+1]
            e = (c+d)/2.0
            b.append(c)
            b.append(e)
        b.append(a[-1])
        return na(b)

    def double_interp_2D_array(a):
        b = double_interp_1D_array(a[:,0])
        c = double_interp_1D_array(a[:,1])
        d = zeros((len(b),2))
        d[:,0] = b
        d[:,1] = c
        return d

    def xys_2_3D(
        xys,
        height_in_pixels = 94,
        width_in_pixels = 168,
        backup_parameter=1,
        ignore_False=True,
    ):
        import k3.misc.fit3d as fit3d
        c = []
        for i in rlen(xys):
            a = xys[i,:]
            b = fit3d.point_in_3D_to_point_in_2D(
                a,
                height_in_pixels=height_in_pixels,
                width_in_pixels=width_in_pixels,
                backup_parameter=backup_parameter,
            )
            if ignore_False and False in b:
                continue
            c.append(b)

        return c








#import kzpy3.Array.fit3d as fit3d
import k3.misc.fit3d as fit3d