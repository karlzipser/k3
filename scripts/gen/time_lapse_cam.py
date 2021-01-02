from k3.utils import *


A = get_Arguments(
    {
        ('t','sleep time (s)'):10,
        ('s','show'):True,
        ('f','flip left right'):False,
        ('p','path'):opjh('scratch'),
        ('d','image difference threshold'):190000000,
        ('m','max sleep time(s)'):60,
    }
)
sleeptime = A['t']
show_frame = A['s']
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
            #figure(1);clf();plot(img_dif);spause()
            print(img_dif[-1])


        if len(img_dif) >= 10:
            if img_dif[-1] > A['d']:  #2 * np.std(na(img_dif)):# [-10:])):
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
            fname = opj(path,d2p(dp(time.time()),'jpg'))
            print(fname)
            imsave(fname,frame)#rgbframe)

        if show_frame:
            if record:
                frame[5:20,2:20,:]=[0,0,255]
            cv2.imshow('Video',frame)# np.fliplr(scipy.misc.imresize(frame,100)))



    time.sleep(0.001)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
