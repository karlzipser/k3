from k3.utils import *

#,tcam.a
"""
python3 k3/scripts/gen/time_lapse_cam.py\
    --mint .1\
    --show\
    --long 3.\
    --diff 117062205.\
    --desired 10\
    --max 10\
    --camera 0\
    --flip True\
    --gtime 0.5\
"""
#,tcam.b




def q(img,xys,xscale=1.,xoffset=0.,yscale=1.,yoffset=0.,sym='.-',thickness=1):
    x,x_prev = False,False
    for xy in xys:
        x_,y_ = xy[0],xy[1]
        if type(x) is not bool:
            x_prev = x
            y_prev = y
        x = intr(x_ * xscale)
        y = intr(y_ * yscale)
        if 'r' in sym:
            color = (255,0,0)
        elif 'b' in sym:
            color = (0,0,255)
        else:
            color = (255,255,0)
        if '.' in sym:
            cv2.circle(img,(x,y),4,color,5)
        if '-' in sym:
            if type(x_prev) is not bool:
                cv2.line(img,(x_prev,y_prev),(x,y),color,thickness)

A = get_Arguments(
    {
        ('mint','min timestep (s)'):10.,
        ('show','show'):True,
        ('flip','flip left-right'):False,
        ('path','path'):opjh('scratch'),
        ('diff','image difference diff_'):190000000.,
        ('long','longer interval (s)'):60.,
        ('desired','desired # shots in long interval'):5,
        ('record','record for real'):False,
        ('graph','show graph'):False,
        ('beep','beep'):False,
        ('camera','0 = internal, 1 = USB camera'):0,
        ('max','max recording time (min)'):10,
        ('gtime','interval between graph plots'):0.1,
    },
    file=__file__,
)
exec(A_to_vars_exec_str)


video_capture = cv2.VideoCapture(camera_)

d = datetime.date.today()

short_timer = Timer(mint_)
long_timer = Timer(long_)
max_timer = Timer(max_*60)
graph_timer = Timer(gtime_)

path = opj(
    path_,
    str(d.year),
    str(d.today().month),
    str(d.today().day),
    'timelapse.'+time_str()
)

os_system('mkdir -p',path,e=1)

last_time = 0

img_dif = []

shot_times = []

frame,prev_frame = False,False

graph_change_timer = Timer(1/2)


graph_off = True

offset = 100 # this is because of a specific camera glitch

while True:

    if max_timer.check():
        break

    if short_timer.rcheck():

        if type(frame) is not bool:
            prev_frame = frame
            

        ret, frame = video_capture.read()

        if type(prev_frame) is not bool:

            frame_diff = (prev_frame[offset:,:,:].astype(float) - frame[offset:,:,:].astype(float) )**2
            #mci(z55(frame_diff),title='diff')
            
            img_dif.append( 
                
                sum(sum(sum(frame_diff)))
            )
            
            if graph_:
                if graph_timer.rcheck():

                    if graph_off:
                        graph_off = False
                        figure(1,figsize=(8,1.5))
                    clf()
                    ln = min(len(img_dif),50)
                    plot(img_dif[-ln:],'k')
                    if record_:
                        line_color = 'r'
                    else:
                        line_color = 'g'
                    plot([0,ln],[diff_,diff_],line_color)
                    
                    ylim([0,5*diff_])
                    spause()
            else:
                plt.close('all')
                graph_off = True

        if len(img_dif) > 0 and img_dif[-1] > diff_:
            record = True
        else:
            record = False

        if long_timer.check():
            long_timer.reset()
            record = True

        last_time = time.time()

        if record:

            shot_times.append(time.time())

            fname_ = opj(path,d2p(dp(time.time()),'jpg'))

            if record_:
                q = '* '
            else:
                q = '- '
            print(q+fname(fname_))
            if beep_:
                beep()
            if record_:
                imsave(fname_,frame)#rgbframe)

        if show_:

            if flip_:
                frame__ = cv2.flip(frame,1)
            else:
                frame__ = frame.copy()


            if record:
                if record_:
                    c = [0,0,255]
                else:
                    c = [0,255,0]
                frame__[5:105,5:105,:]=c
            


            cv2.imshow('Video',frame__)# np.fliplr(scipy.misc.imresize(frame,100)))



    time.sleep(0.001)
    
    k = cv2.waitKey(1)

    if k != -1:
        print('k =',k)

    if  k & 0xFF == ord('q') or k == 27: #ESC
        break

    elif k & 0xFF == ord('g') or k == 2: # left arrow
        print('graph_ =',graph_)
        if graph_change_timer.rcheck():
            graph_ = not graph_

    elif k & 0xFF == ord('r') or k == 3: # right arrow
        record_ = not record_

    elif k & 0xFF == ord('u') or k == 0: # up arrow
        diff_ *= 1.1
        print('diff_',dp(diff_))

    elif k & 0xFF == ord('d') or k == 1: # down arrow
        diff_ *= (1/1.1)
        print('diff_',dp(diff_))

    
video_capture.release()
cv2.destroyAllWindows()

#EOF

