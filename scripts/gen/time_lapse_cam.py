from k3.utils import *

#,tcam.a
"""
python3 k3/scripts/gen/time_lapse_cam.py\
    -t .1\
    -s\
    -f False\
    -m 30.\
    -d 117062205.\


"""
#,tcam.b


# long interval, max num shots in long interval, short interval, total duration
A = get_Arguments(
    {
        ('t','sleep time (s)'):10.,
        ('s','show'):True,
        ('f','flip left right'):False,
        ('p','path'):opjh('scratch'),
        ('d','image difference threshold'):190000000.,
        ('m','max sleep time(s)'):60.,
        ('r','record for real'):False,
        ('g','show graph'):False,
        ('b','beep'):False,
    }
)
sleeptime = A['t']
show_frame = A['s']
record_for_real = A['r']
threshold = A['d']

video_capture = cv2.VideoCapture(0)
d = datetime.date.today()
path = opj(
    A['p'],
    str(d.year),
    str(d.today().month),
    str(d.today().day),
    'timelapse.'+time_str()
)
print(path)
os_system('mkdir -p',path)

last_time = 0

img_dif = []
frame,prev_frame = False,False
max_sleep = Timer(A['m'])

while True:

    if time.time()-last_time > sleeptime:
        if type(frame) is not bool:
            prev_frame = frame
        ret, frame = video_capture.read()

        if type(prev_frame) is not bool:
            img_dif.append( 
                sum(sum(sum(( prev_frame.astype(float) - frame.astype(float) )**2))))
            
            if A['g']:
                figure(1)
                clf()
                plot(img_dif)
                plot([0,len(img_dif)],[threshold,threshold],'r')
                ylim([0,5*threshold])
                spause()
            else:
                plt.close('all')
            #print(img_dif[-1])


        if len(img_dif) >= 10:
            if img_dif[-1] > threshold:  #2 * np.std(na(img_dif)):# [-10:])):
                record = True
            else:
                record = False
        else:
            record = True

        if max_sleep.check():
            max_sleep.reset()
            record = True

        last_time = time.time()

        if record:
            fname_ = opj(path,d2p(dp(time.time()),'jpg'))

            if record_for_real:
                q = '* '
            else:
                q = '- '
            print(q+fname(fname_))
            if A['b']:
                beep()
            if record_for_real:
                imsave(fname_,frame)#rgbframe)

        if show_frame:
            if record:
                if record_for_real:
                    c = [0,0,255]
                else:
                    c = [0,255,0]
                frame[5:20,2:20,:]=c
            cv2.imshow('Video',frame)# np.fliplr(scipy.misc.imresize(frame,100)))



    time.sleep(0.001)
    
    k = cv2.waitKey(1)

    if  k & 0xFF == ord('q'):
        break

    elif k & 0xFF == ord('r'):
        record_for_real = not record_for_real

    elif k & 0xFF == ord('u'):
        threshold *= 1.1
        print('threshold',dp(threshold))

    elif k & 0xFF == ord('d'):
        threshold *= (1/1.1)
        print('threshold',dp(threshold))

    elif k & 0xFF == ord('g'):
        print(A['g'])
        A['g'] = not A['g']

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
