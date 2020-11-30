
#,a
from k3 import *

if 'Arguments':

    Arguments = get_Arguments(
        {
            'run':REQUIRED,
            'start':0,
            'stop':-1,
            'mod':1,
            'use_past':True,
            'path_step':5,
            'print_motor_encoder':False,
            'past_back_steps':30,
            'future_back_steps':5,
        }
    )

    if Arguments['use_past']:
        past_future_list = ['past','future']
    else:
        past_future_list = ['future']

    zprint(Arguments)

    if len(sggo(opjD('Data/train/h5py',Arguments['run']))) > 0:
        run_type = 'train'
        #assert False
    elif len(sggo(opjD('Data/validate/h5py',Arguments['run']))) > 0:
        run_type = 'validate'
    else:
        clp(Arguments['run'],'not found')
        assert False



if 'load run data':

    if 'L' not in locals():
        try:
            L=h5r(opjD('Data',run_type,'h5py',Arguments['run'],'left_timestamp_metadata_right_ts.h5py'))
        except:
            L=h5r(opjD('Data',run_type,'h5py',Arguments['run'],'left_timestamp_metadata.h5py'))
        cm('opened L')
        O = h5r(opjD('Data',run_type,'h5py',Arguments['run'],'original_timestamp_data.h5py'))
        cm('opened O')

    if 'Y' not in locals():
        Y = lo(opjD('Data/outer_contours/output_2_data',run_type,Arguments['run']+'.pkl'))

    start = Arguments['start']
    if Arguments['stop'] < 0:
        stop = len(L['motor'])
    else:
        stop = Arguments['stop']
    print_timer = Timer(1/70.)
    alpha = 0
    xyi = na([[0,0,0]])
    sample_frequency = 30


    if 'UO' not in locals():
        cm('Building UO...')
        t0 = time.time()
        UO = {
            'past':{
                'range':(21,26),#(23,24),
                'back_steps':Arguments['past_back_steps']*sample_frequency,
                'S':{},
            },
            'future':{
                'range':(21,66),
                'back_steps':Arguments['future_back_steps'],
                'S':{},
            },
        }

        for k in ['past','future']:
            a,b = UO[k]['range']
            for i in range(start,stop,1):
                if i not in Y:
                    continue
                UO[k]['S'][i] = {
                    'left': Y[i]['outer_countours_rotated_left'][a:b,:],
                    'right':  Y[i]['outer_countours_rotated_right'][a:b,:],
                    'angles_left': Y[i]['angles_left'][a:b],
                    'angles_right':  Y[i]['angles_right'][a:b],
                    'index':i,
                    'steps_left':0,
                }
        soD(UO,'UO')
        cm('Made UO in',dp(time.time()-t0),'seconds')
    else:
        t0 = time.time()
        UO = loD('UO')
        cm('in',time.time()-t0,'seconds')




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




def plot_3D_points_in_image(xys,color='r',sym='o',max_range=5,border=5,doubles=5):
    xys = na(xys)
    for q in range(doubles):
        if len(xys) > 0:
            xys = double_interp_2D_array(xys)
    a = []
    for i in rlen(xys):
        if np.sqrt(xys[i,0]**2 +xys[i,1]**2) < max_range:
            a.append(xys[i,:])

    pts = na(xys_2_3D(na(a)))
    #raw_enter()
    if len(pts) > 0:
        border_point = na([border,border])
        pts_plot(border_point+pts,sym=sym,ms=2,color=color)





_LARGER_IMAGES = {}
def mi_bordered_image(img,figure_num=1,border=5,img_title='title'):
    height,width,__ = shape(img)
    if img_title not in _LARGER_IMAGES:
        _LARGER_IMAGES[img_title] = zeros((height+2*border,width+2*border,3),np.uint8)
    _LARGER_IMAGES[img_title][border:border+height,border:border+width,:] = img
    mi(_LARGER_IMAGES[img_title],figure_num,img_title=img_title)

   

import warnings
warnings.filterwarnings("ignore")
from scipy.optimize import curve_fit

def f___(x,A,B):
    return A*x+B

def get_offshoot(A,B,r,theta):
  m,b = curve_fit(f___,(A[0],B[0]),(A[1],B[1]))[0]
  alpha = corrected_angle(m,B,A)
  C = B + na([0,r])
  D = rotatePoint(B,C,90-theta+alpha+0)
  return D




if 'path functionality':

    PATH = [na([0,0])]

    def grow_path(heading,encoder,motor,xyi,alpha,i,back_steps):

        a = vec(heading,encoder,motor)
        PATH.append(PATH[-1]+a)


        if len(xyi) > 1:

            alpha_prev = alpha
            alpha = 90 - get_alpha([[0,0],a])

            d_alpha = alpha - alpha_prev

            xy = xyi[:,:2]

            xy -= xy[-1]

            xyi[:,:2] = xy


            xyi[:,:2] = rotate_alpha(d_alpha, xyi[:,:2])

        else:
            d_alpha = 0

        xyi = np.concatenate((xyi, na([[ 0, magnitude(a), i ]])))

        if len(xyi) > back_steps:
            xyi = xyi[-back_steps:]

        return xyi,alpha,d_alpha,a


    times = {
        'grow_path':[],
        'past_future':[],
        'graphics':[],
    }
    times_mean = {
        'grow_path':0,
        'past_future':0,
        'graphics':0,
    }



Colors = {'direct':'b','left':'r','right':'g'}
U = UO

for i in range(start,stop):

    if 'drive_mode' in L and not L['drive_mode'][i]:
        continue

    if Arguments['print_motor_encoder']:
        print('motor',dp(L['motor'][i]),'encoder',dp(L['encoder'][i]))

    if L['motor'][i] < 52 or L['encoder'][i] < 1.5:
            continue

    t0 = time.time()
    xyi,alpha,d_alpha,a = grow_path(
        L['gyro_heading_x_meo'][i],
        L['encoder_meo'][i],
        L['motor'][i],
        xyi,
        alpha,
        i,
        1 * sample_frequency,
    )

    times['grow_path'].append(time.time()-t0)


    t0 = time.time()

    for k in past_future_list:

        S = U[k]['S']

        for j in S:

            if j > i:
                continue

            R = S[j]

            if R['index'] == i:

                R['steps_left'] = U[k]['back_steps']


            if R['steps_left']:

                R['steps_left'] -= 1

                for s in ['left','right']:

                    R[s] -= na([[0,magnitude(a)]])
                    R[s] = rotate_alpha(d_alpha, R[s])

                assert R['steps_left'] >= 0

                

    times['past_future'].append(time.time()-t0)


    if 'graphics':
        t0 = time.time()
        e = 100
        plot_top_view = False
        if i % Arguments['mod'] == 0:
            xy = xyi[:,:2]
            if plot_top_view:
                figure(1)
                clf()
                plot([-e,e],[0,0],'k:')
                plot([0,0],[-e,e],'k:')
                pts_plot(xy,sym='.',color='c',ms=4)
            
            W = { 'past':{'left':None,'right':None}, 'future':{'left':None,'right':None} }
            for k in past_future_list:
                T = {'left':0,'right':0}
                #lctr = 0.0
                #rctr = 0.0
                Ctr = {'left':0,'right':0}
                
                S = U[k]['S']
                
                for j in S:
                    
                    R = S[j]
                    for side in ['left','right']:
                        if R['steps_left']:
                            Ctr[side] += 1

                            #print(R['angles_'+side])
                            #print(R[side])

                            E = {'left':[(0,0)],'right':[(0,0)]}

                            for j in rlen(R['angles_'+side]):
                                a = R['angles_'+side][j]
                                a = min(np.abs(a),400)
                                marker_size = int(a/2.)
                                #pts_plot(b['outer_countours_rotated_'+s][j] + o['xy'][i],Colors[s],sym='.',ms=marker_size)
                                if j > 0:
                                    if side == 'left':
                                        aa = 180 - a
                                    else:
                                        aa = a - 180
                                    D = get_offshoot( 
                                        R[side][j-1],
                                        R[side][j],
                                        np.abs(a)/30.,
                                        aa,
                                    )
                                    E[side].append(D)
                            
                            R[side] = na(E[side])

                            T[side] += R[side]

                            if plot_top_view:
                                pts_plot(R[side],sym='.',ms=2,color=Colors[side])

                for side in ['left','right']:
                    W[k][side] = T[side] / Ctr[side]
                    if plot_top_view:
                        pts_plot(W[k][side],sym='-',ms=2,color='k')

            if plot_top_view:
                if Arguments['use_past']:
                    xylim(-50,50,-50,30)
                else:
                    xylim(-15,15,-1,30)
                plt_square()
                plt.title(i)
                spause()















            mi_bordered_image(O['left_image']['vals'][i],figure_num=2,border=5,img_title=d2s('left_image',i))
            
            plot_3D_points_in_image(W['future']['left'][:4,:],color='r',sym='o-',max_range=95,border=5,doubles=5)
            plot_3D_points_in_image(W['future']['left'][3:,:],color='r',sym='o-',max_range=95,border=5,doubles=0)
            
            plot_3D_points_in_image(W['future']['right'][:,:],color='g',sym='o',max_range=95,border=5,doubles=5)

            spause()

            if save_3D_points_in_image:
                plt.savefig(
                    opj(fig_path,d2p(time_string,figname,jpeg)),
                    format='jpeg'
                )



            show_PATH = False
            if show_PATH:
                if len(PATH) > Arguments['path_step']:
                    figure(10)
                    clf()
                    plt_square()
                    pts_plot(PATH[0:len(PATH):Arguments['path_step']],color='k')

                

    times['graphics'].append(time.time()-t0)
    

    if i % 100 == 0:
        for k in times.keys():
            times_mean[k] = na(times[k]).mean()
        kprint(times_mean,'times_mean')



#,b


#EOF

