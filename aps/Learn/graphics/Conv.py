from k3 import *

CA()

graphics_timer = None
#W = {}
e = 24


if 'rotate in 3d':
    #https://stackoverflow.com/questions/6802577/rotation-of-3d-vector
    import numpy as np
    import math

    def rotation_matrix(axis, theta):
        """
        Return the rotation matrix associated with counterclockwise rotation about
        the given axis by theta radians.
        """
        axis = np.asarray(axis)
        axis = axis / math.sqrt(np.dot(axis, axis))
        a = math.cos(theta / 2.0)
        b, c, d = -axis * math.sin(theta / 2.0)
        aa, bb, cc, dd = a * a, b * b, c * c, d * d
        bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
        return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                         [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                         [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])

    v = [3, 5, 0]
    axis = [4, 4, 1]
    theta = 1.2 

    print((np.dot(rotation_matrix(axis, theta), v))) 
    # [ 2.74911638  4.77180932  1.91629719]





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

def parse_target_vector(v,reverse=False):
    #print shape(v)
    q = 66#42
    assert len(v) == 6*q
    lx = v[0:q]
    rx = v[q:2*q]
    ly = v[2*q:3*q] * 10
    ry = v[3*q:4*q] * 10
    al = v[4*q:5*q] * 10
    ar = v[5*q:6*q] * 10
    if reverse:
        lx *= -1
        rx *= -1
        al *= -1
        ar *= -1
    outer_countours_rotated_left = zeros((q,2))
    outer_countours_rotated_left[:,0] = lx
    outer_countours_rotated_left[:,1] = ly

    outer_countours_rotated_right = zeros((q,2))
    outer_countours_rotated_right[:,0] = rx
    outer_countours_rotated_right[:,1] = ry

    angles_left = al
    angles_right = ar

    return outer_countours_rotated_left, outer_countours_rotated_right, angles_left, angles_right,

Colors = {'direct':'b','left':'r','right':'g'}

def plot_map(
    outer_countours_rotated_left,
    outer_countours_rotated_right,
    angles_left,
    angles_right,
    color='k',
    name='map',
    e = 24,
    marker_size_divisor = 4.0,
    grid=True,
):
    D = {
            'angles' : {
                'left' :     angles_left,
                'right' :    angles_right,
            },
            'outer_countours_rotated' : {
                'left' :     outer_countours_rotated_left,
                'right' :    outer_countours_rotated_right,
            },
            'marker_size' : {
                'left' :     angles_left,
                'right' :    angles_right,
            },
            #'turns' : M['turns'][i].copy(),
    }

    for k in ['left','right']:
        for l in rlen(D['marker_size'][k]):
            a = min(np.abs(D['marker_size'][k][l]),80)
            marker_size = int(a/marker_size_divisor)
            D['marker_size'][k][l] = marker_size
 

    if 'plot rotated' and 'outer_countours_rotated' in D:
        
        figure(name); plt_square(); xylim(-e,e,-e,e)

        if grid:
            plot([-e,e],[0,0],'k:')
            plot([0,0],[-e,e],'k:')

        for k in ['left','right']:
            xy = D['outer_countours_rotated'][k]
            plot(xy[:,0],xy[:,1],color+'-',linewidth=1)
            for r in rlen(D['outer_countours_rotated'][k]):
                pts_plot(D['outer_countours_rotated'][k][r],Colors[k],sym='.',ms = D['marker_size'][k][r])





fig_path = None

save_timer = Timer(60)


Pts_prev = {'output_2':None,'target':None}
s = 0.5

def graphics_function(N,M,P):#,X):

    global graphics_timer
    global fig_path
    if fig_path is None:
        fig_path = opjD('Data/outer_contours/figures-'+P['single_run'])
        fig_path = opj('/Volumes/osx-data/figures-'+P['single_run'])
        os.system('mkdir -p '+fig_path)

    P['hide_target'] =True
    P['hide_target_output_figure'] =True
    P['hide_loss'] =True
    P['hide_output_2'] =True
    P['hide_meta'] =True
    P['hide_3d_output2'] =False
    P['hide_3d_target'] =True

    
    if graphics_timer == None:
        graphics_timer = Timer(M['Q']['runtime_parameters']['graphics_timer_time'])
        graphics_timer.trigger()




    if k_in_D('save_output_2',P):
        #cm(1,r=1)
        cb(P['ctr'])

        
        output_2 = N.extract('output_2')

        outer_countours_rotated_left, outer_countours_rotated_right, angles_left, angles_right = parse_target_vector(output_2)

        P['output_2_data'][P['ctr']] = {
            'outer_countours_rotated_left':outer_countours_rotated_left,
            'outer_countours_rotated_right':outer_countours_rotated_right,
            'angles_left':angles_left,
            'angles_right':angles_right,
        }
        if not 'graphics':
            figure(99)
            clf();plt_square()
            pts_plot(P['output_2_data'][P['ctr']]['outer_countours_rotated_left'],'r')
            pts_plot(P['output_2_data'][P['ctr']]['outer_countours_rotated_right'],'g')
            spause()
        if save_timer.check():
            os.system(d2s('mkdir -p',opjD('Data/outer_contours/output_2_data')))
            soD(opjD('Data/outer_contours/output_2_data',P['run']),P['output_2_data'])
            cg('saving',P['run'],'output_2_data',P['ctr'])
            save_timer.reset()
        return
        #graphics_timer.trigger()

    #cm(2,r=1)



    cv2.waitKey(1)
    if graphics_timer.time_s != M['Q']['runtime_parameters']['graphics_timer_time']:
        graphics_timer.trigger()


    time_string = d2p(P['run'],P['ctr']) ## removed from if below

    if False:#'save_figures' in P:
        if P['save_figures'] > 0:
            cb("P['save_figures'] =",P['save_figures'])
            time_string = d2p(P['run'],P['ctr'])
            graphics_timer.trigger()
            P['save_figures'] -= 1
            if P['save_figures'] < 0:
                P['save_figures'] = 0
        else:
            cg('done saving figures')
            sys.exit(0)
    #cm(3,r=1)
    #cm(M['Q']['runtime_parameters']['graphics_timer_time'])
    if graphics_timer.check() or M['Q']['runtime_parameters']['graphics_timer_time'] < 0:
        #cm('here')
        if M['Q']['runtime_parameters']['graphics_timer_time'] == -2:
            raw_enter()
        if False:
            M['load']()
        graphics_timer = Timer(M['Q']['runtime_parameters']['graphics_timer_time'])
    else:
        return

    title_name = title='.'.join(P['type'])
    #cm(4,r=1)
    if not P['hide_loss']:
        
        figure(P['type'][-1],figsize=(2,10))
        clf()

        n = int(M['Q']['runtime_parameters']['percent_loss_to_show']/100.0 * len(N.losses))
        plot(N.losses[-n:],'.')
        m = meo(na(N.losses[-n:]),M['Q']['runtime_parameters']['meo_num'])
        plot(m)
        mm = na(m[int(len(m)/2):])
        mn,mx = 0,1
        if len(M['Q']['runtime_parameters']['graphics_ylim']) == 2:
            mn = M['Q']['runtime_parameters']['graphics_ylim'][0]
            mx = M['Q']['runtime_parameters']['graphics_ylim'][1]
            #print mn,mx
        elif len(mm) > 5 :
            #av = mm.mean()
            av=0
            std = mm.std()
            #mx = (mm.max()-av) * 1.3# + av
            #mn = (mm.min()-av) * 0.8# + av
            mn = mm.mean()-std*M['Q']['runtime_parameters']['loss_stds']
            mx = mm.mean()+std*M['Q']['runtime_parameters']['loss_stds']
        #print(std,mn,mx)
        if type(mn) == float and type(mx) == float:
            ylim(
                mn,
                mx,
            )
    #cm(5,r=1)
    Imgs = {}
    img_lst = []
    img_spacer = False
    k_prev = 'input'
    for k in ['input']:#,'output','target']:
        Imgs[k] = N.extract(k)

        if 'display.'+k in P:
            lst = P['display.'+k]
            for i in range(0,len(lst),2):
                start = int(lst[i])
                stop = int(lst[i+1])
                img = Imgs[k][start:stop,:,:]
                img = z55(img.transpose(2,1,0))
                if False:#k == 'input':
                    r = img[:,:168,0].copy()
                    g = img[:,:168,1].copy()
                    b = img[:,:168,2].copy()
                    img[:,:168,0] = b
                    img[:,:168,1] = g
                    img[:,:168,2] = r

                if k_prev != k:
                    k_prev = k
                    if type(img_spacer) == type(False):
                        img_spacer = 255+0*img[:,:10,:]
                    img_lst.append(img_spacer)

                img_lst.append(img)

    #cm(6,r=1)
    output_2 = N.extract('output_2')
    target = N.extract('target')
    meta = N.extract('meta')

    if False:
        figure('target-output',figsize=(4,3));clf();
        plot(output_2,'r.')
        plot(target,'k.')

    #cm(7,r=1)

    if 'mapping1':
        outer_countours_rotated_left, outer_countours_rotated_right, angles_left, angles_right = parse_target_vector(target)
        #cm(8,r=1)

        if not P['hide_target_output_figure']:
            figure('map');clf()

            plot_map(
                outer_countours_rotated_left,
                outer_countours_rotated_right,
                angles_left,
                angles_right,
                color='k',
                name='map',
                e=e,
                grid=True,
            )

        outer_countours_rotated_left, outer_countours_rotated_right, angles_left, angles_right = parse_target_vector(output_2)

        if not P['hide_target_output_figure']:
            plot_map(
                outer_countours_rotated_left,
                outer_countours_rotated_right,
                angles_left,
                angles_right,
                color='b',
                name='map',
                e=e,
                grid=False,
            )

            if k_in_D('save_figures',P):
                plt.savefig(opj(fig_path,d2p(time_string,'map','pdf')),format='pdf')






        import k3.misc.fit3d as fit3d

        im = N.extract('input')
        im = z55(im.transpose(2,1,0))

        
        for data,name in ((output_2,'output_2'),(target,'target')):
        #data,name = output_2,'output_2'
            if name == 'target' and P['hide_3d_target']:
                continue
            if name == 'output_2' and P['hide_3d_output2']:
                continue

            outer_countours_rotated_left, outer_countours_rotated_right, angles_left, angles_right = parse_target_vector(data)
            figname = 'map3d-'+name
            figure(figname);clf()

            mi(im,figname)
            plt.title(d2s(P['single_run'],P['gctr']))
            for o,color in ((outer_countours_rotated_left,'r'),(outer_countours_rotated_right,'g')):
                c = []
                w = double_interp_2D_array(o[:33,:])
                w = double_interp_2D_array(w)
                w = double_interp_2D_array(w)
                o = np.concatenate((w,o[33:,:]))

                #ctr = 0
                for i in rlen(o):
                    a = o[i,:]
                    b = fit3d.point_in_3D_to_point_in_2D(
                        a,
                        height_in_pixels = 94,
                        width_in_pixels = 168,
                        backup_parameter=1,
                    )
                    p = 3
                    if False not in b:
                        #cm(b)
                        if b[0] > p and b[0] < 168-p:
                            #cy(b)
                            if b[1] > p and b[1] < 94-p:
                                #cg(b)
                                c.append(b)
                                #print(int(c[-1][1]))
                    #ctr += 1
                #cm('ctr',ctr)
                c = na(c)
                if False:
                    if Pts_prev[name] is None:
                        Pts_prev[name] = c
                    cm(shape(c),shape(Pts_prev[name]))
                    if shape(c) == shape(Pts_prev[name]):
                        cm('here')
                        c = s * c + (1-s) * Pts_prev[name]
                    Pts_prev[name] = c
                try:
                    pts_plot(c,color=color,sym='.')
                except:
                    clp('Exception, shape(c) =',shape(c),'`wrb')

            if k_in_D('save_figures2',P):
                if P['save_figures2'] != 'no':
                    fmt = 'pdf' 
                    if type(P['save_figures2']) is str:
                        fmt = P['save_figures2']                    
                    plt.savefig(opj(fig_path,d2p(time_string,figname,fmt)),format=fmt)



        outer_countours_rotated_left, outer_countours_rotated_right, angles_left, angles_right = parse_target_vector(target)

        if not P['hide_target']:
            figure('map target');clf()

            plot_map(
                outer_countours_rotated_left,
                outer_countours_rotated_right,
                angles_left,
                angles_right,
                color='k',
                name='map target',
                e=e,
                #x_offset=-0,
            )

        outer_countours_rotated_left, outer_countours_rotated_right, angles_left, angles_right = parse_target_vector(output_2)


        if not P['hide_output_2']:
            figure('map output_2');clf()

            plot_map(
                outer_countours_rotated_left,
                outer_countours_rotated_right,
                angles_left,
                angles_right,
                color='b',
                name='map output_2',
                e=e,
                #x_offset=0,
            )
            cg(P['ctr'])
            if k_in_D('save_figures',P):
                plt.savefig(opj(fig_path,d2p(time_string,'map_output_2','pdf')),format='pdf')





    if not P['hide_meta']:
        figure('meta',figsize=(3,3))
        meta[4,0,0] = 1
        meta[4,0,1] = 2
        meta[4,0,2] = 3
        mi(meta[4,:,:],'meta')


    spause()

    concatt = None
    while len(img_lst) > 0:
        img = img_lst.pop(0)
        if type(concatt) == type(None):
            concatt = img.copy()
            #print 'a',shape(concatt),shape(img)
        else:
            #print 'b',shape(concatt),shape(img)
            concatt = np.concatenate((concatt,img),axis=1)
    if False:
        mci(concatt,1,scale=M['Q']['runtime_parameters']['scale'],title=title_name)

    if k_in_D('save_figures',P):
        plt.savefig(opj(fig_path,d2p(time_string,'meta','pdf')),format='pdf')


    if M['Q']['runtime_parameters']['save_images']:
        path = opjD('__TEMP__',fname(P['NETWORK_OUTPUT_FOLDER']))
        print(path)
        os.system(d2s('mkdir -p',path))
        imsave(opj(path,str(time.time())+'.png'),img)


    spause()

    #if k_in_D('save_figures',P):
    #    cm('ready to save figure',ra=1)


#EOF



