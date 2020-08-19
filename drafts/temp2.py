#,a


from k3.vis3 import *
from PIL import Image, ImageDraw

if 'frames' not in locals():
    import mmcv
    video = mmcv.VideoReader(opjD("temp/1/temp.mp4"))
    frames = [Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)) for frame in video]

import k3.drafts.F as F
Network = F.F()

skip = 1
rng = list(range(0,len(frames),skip))

for i in rng:
    frame = frames[i].resize(na((160,120))*2)

    boxes = Network.process_frame( frame )

    frame_draw = frame.copy()
    draw = ImageDraw.Draw(frame_draw)
    try:
        for box in boxes:
            draw.rectangle(box.tolist(), outline=(255, 0, 0), width=6)
    except:
        pass
    mci(na(frame_draw),delay=1)

#,b

#EOF
