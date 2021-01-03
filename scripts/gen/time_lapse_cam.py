from k3.utils import *

#,tcam.a
"""
python3 k3/scripts/gen/time_lapse_cam.py\
    --mint .1\
    --show\
    --long 3.\
    --diff 117062205.\
    --desired 10\
"""
#,tcam.b


A = get_Arguments(
    {
        ('mint','min timestep (s)'):10.,
        ('show','show'):True,
        ('flip','flip left right'):False,
        ('path','path'):opjh('scratch'),
        ('diff','image difference diff_'):190000000.,
        ('long','longer interval (s)'):60.,
        ('desired','desired # shots in long interval'):5,
        ('record','record for real'):False,
        ('graph','show graph'):False,
        ('beep','beep'):False,
        ('camera','0 = internal, 1 = USB camera'):0,
    },
    file=__file__,
)


exec(A_to_vars_exec_str)



video_capture = cv2.VideoCapture(camera_)

d = datetime.date.today()

long_timer = Timer(long_)

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

while True:

    if time.time()-last_time > mint_:

        if type(frame) is not bool:
            prev_frame = frame

        ret, frame = video_capture.read()

        if type(prev_frame) is not bool:
            offset = 100 # this is because of specific camera glitch
            img_dif.append( 
                
                sum(sum(sum(
                    (prev_frame[offset:,:,:].astype(float) - frame[offset:,:,:].astype(float) )**2
                )))
            )
            
            if graph_:
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
            if record:
                if record_:
                    c = [0,0,255]
                else:
                    c = [0,255,0]
                #frame[:100,:,:]=255
                frame[5:105,5:105,:]=c
            cv2.imshow('Video',frame)# np.fliplr(scipy.misc.imresize(frame,100)))



    time.sleep(0.001)
    
    k = cv2.waitKey(1)

    if  k & 0xFF == ord('q'):
        break

    elif k & 0xFF == ord('g'):
        print('graph_ =',graph_)
        if graph_change_timer.rcheck():
            graph_ = not graph_

    elif k & 0xFF == ord('r'):
        record_ = not record_

    elif k & 0xFF == ord('u'):
        diff_ *= 1.1
        print('diff_',dp(diff_))

    elif k & 0xFF == ord('d'):
        diff_ *= (1/1.1)
        print('diff_',dp(diff_))

    
video_capture.release()
cv2.destroyAllWindows()

#EOF

