from facenet_pytorch import MTCNN
import torch
import numpy as np
import mmcv, cv2
from PIL import Image, ImageDraw
from IPython import display

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print('Running on device: {}'.format(device))


mtcnn = MTCNN(keep_all=True, device=device)

video = mmcv.VideoReader(opjD("temp/1/temp.mp4"))
#video = mmcv.VideoReader(opjD("/Users/karlzipser/Desktop/03940FF3-4F85-45F5-925E-F1C8C90DCA39_3 copy.mov"))
frames = [Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)) for frame in video]

#display.Video('video.mp4', width=640)


#,a
skip = 1
frames_tracked = []
rng = list(range(0,len(frames),skip))
#random.shuffle(rng)
for i in rng:
    frame = frames[i]
    boxes, _ = mtcnn.detect(frame)
    if boxes is None:
        lb = 0
    else:
        lb = len(boxes)
    clp(i,')',lb)
    #if lb < 1:
    #    continue
    frame_draw = frame.copy()
    draw = ImageDraw.Draw(frame_draw)
    if lb > 0:#try:
        for box in boxes:
            draw.rectangle(box.tolist(), outline=(255, 0, 0), width=6)
    else:#except:
        pass
    frames_tracked.append(frame_draw.resize((640, 360), Image.BILINEAR))
    mci(na(frames_tracked[-1]),delay=1)
print('\nDone')

#,b

if False:
    d = display.display(frames_tracked[0], display_id=True)
    i = 1
    try:
        while True:
            d.update(frames_tracked[i % len(frames_tracked)])
            i += 1
    except KeyboardInterrupt:
        pass


    dim = frames_tracked[0].size
    fourcc = cv2.VideoWriter_fourcc(*'FMP4')    
    video_tracked = cv2.VideoWriter('video_tracked.mp4', fourcc, 25.0, dim)
    for frame in frames_tracked:
        video_tracked.write(cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR))
    video_tracked.release()



#EOF
