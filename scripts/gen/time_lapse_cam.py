from k3.utils import *

#,tcam0.a
"""
python3 k3/scripts/gen/time_lapse_cam.py\
    --mint 1.\
    --show\
    --long 20.\
    --diff 117062205.\
    --max 120\
    --flip False\
    --gtime 0.5\
    --show_diff False\
    --beep_time 4\
"""
#,tcam0.b


#,tcam1.a
"""
python3 k3/scripts/gen/time_lapse_cam.py\
    --mint .1\
    --show\
    --long 0.3333\
    --diff -1.\
    --max 120\
    --flip False\
    --gtime 0.5\
    --show_diff False\
    --beep_time 30\
    --record\
"""
#,tcam1.b

A = get_Arguments(
    {
        ('mint','min timestep (s)'):10.,
        ('show','show'):True,
        ('flip','flip left-right'):False,
        ('path','path'):opjh('scratch'),
        ('diff','image difference diff_'):190000000.,
        ('long','longer interval (s)'):60.,
        ('record','record for real'):False,
        ('graph','show graph'):True,
        ('beep_time','min beep time'):-1,
        #('camera','0 = internal, 1 = USB camera'):0,
        ('max','max recording time (min)'):60,
        ('gtime','interval between graph plots'):0.1,
        ('tsteps','steps of timeseries to show'):500,
        ('show_diff','difference image'):False,
        ('thickness','line thickness'):2,
        ('cthickness','circle line thickness'):2,
        ('gscale','scale for plot'):1.0,
    },
    file=__file__,
)
exec(A_to_vars_exec_str)


video_capture = cv2.VideoCapture(1)
ret, frame = video_capture.read()

if frame is None:
    #time.sleep(1)
    video_capture.release()
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    if frame is None:
        cE('camera not found')
        assert False

d = datetime.date.today()

short_timer = Timer(mint_)
long_timer = Timer(long_)
max_timer = Timer(max_*60)
graph_timer = Timer(gtime_)
if beep_time_ > 0:
    beep_timer = Timer(beep_time_)

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

offset = 0 # 100 # this is because of a specific camera glitch

ctr = 0

while True:

    if max_timer.check():
        break

    if short_timer.rcheck():

        if type(frame) is not bool:
            prev_frame = frame
            

        ret, frame = video_capture.read()

        if True:#not show_diff_:
            if flip_:
                frame__ = cv2.flip(frame,1)
            else:
                frame__ = frame.copy()

        if type(prev_frame) is not bool:

            frame_diff = (prev_frame[offset:,:,:].astype(float) - frame[offset:,:,:].astype(float) )**2
            #mci(z55(frame_diff),title='diff')
            
            if show_diff_:
                frame__ = z55(frame_diff)
                if flip_:
                    frame__ = cv2.flip(frame__,1)

            img_dif.append( 
                
                sum(sum(sum(frame_diff)))
            )
            
            if graph_:
                if True:#graph_timer.rcheck():

                    ln = min(len(img_dif),tsteps_)

                    if record_:
                        line_color = 'r'
                    else:
                        line_color = 'g'
                    xs = arange(0,tsteps_)
                    ys = 0*xs
                    ys[-ln:] = na(img_dif[-ln:])
                    height,width,_ = shape(frame)
                    x = xtrans(xs,0,max(xs),width)
                    y = xtrans(ys,0,190000000*25*gscale_,width)
                    zplot(frame__,width-x,height-y,'b-',radius=5,thickness=thickness_,cthickness=cthickness_)
                    xs = na([0,1])
                    ys = na([diff_,diff_])
                    x = xtrans(xs,0,1,width)
                    y = xtrans(ys,0,190000000*25*gscale_,width)
                    zplot(frame__,width-x,height-y,'r-',radius=5,thickness=thickness_,cthickness=cthickness_)                    

            else:
                plt.close('all')
                graph_off = True

        if len(img_dif) > 0 and (img_dif[-1] > diff_ and diff_ > 0):
            record = True
        else:
            record = False

        if long_timer.check():
            long_timer.reset()
            record = True

        last_time = time.time()

        if record:

            shot_times.append(time.time())

            

            if record_:
                q = '* '
            else:
                q = '- '
            print(q)#+fname(fname_))

            if record_:
                fname_ = opj(path,d2p(ctr,'jpg'))
                imsave(fname_,frame)#rgbframe)
                ctr += 1
                if beep_time_ > 0 and beep_timer.rcheck():
                    beep()
        if show_:

            if record:
                if record_:
                    c = [0,0,255]
                else:
                    c = [0,255,0]
                frame__[5:205,-205:-5,:]=c
            


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

    elif k == 0: # up arrow
        diff_ *= 1.1
        print('diff_',dp(diff_))

    elif k == 1: # down arrow
        diff_ *= (1/1.1)
        print('diff_',dp(diff_))

    elif k & 0xFF == ord('d'): # down scale
        gscale_ *= 1.1
        print('gscale_',dp(gscale_))

    elif k & 0xFF == ord('u'): # up scale
        gscale_ *= (1/1.1)
        print('gscale_',dp(gscale_))

    elif k & 0xFF == ord('f'):
        flip_ = not flip_

    elif k & 0xFF == ord('s'):
        show_diff_ = not show_diff_

    elif k & 0xFF == ord('1'):
        thickness_ = 1

    elif k & 0xFF == ord('2'):
        thickness_ = 2

    elif k & 0xFF == ord('3'):
        thickness_ = 3

    elif k & 0xFF == ord('4'):
        thickness_ = 4

    elif k & 0xFF == ord('5'):
        thickness_ = 5

    elif k & 0xFF == ord('6'):
        thickness_ = 6

    elif k & 0xFF == ord('7'):
        thickness_ = 7

video_capture.release()
cv2.destroyAllWindows()

#EOF

