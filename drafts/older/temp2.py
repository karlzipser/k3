#,a

from k3.vis3 import *

Arguments = get_Arguments(
    Defaults={
        'src':opjD("temp/1/temp.mp4"),
        'start_percent':0,
        'end_percent':100,
        'scale_divider':1,
    }
)
kprint(Arguments)


if 'frames' not in locals():
    from PIL import Image
    import mmcv
    video = mmcv.VideoReader(Arguments['src'])
    l = len(video)
    a = int(l*Arguments['start_percent']/100)
    b = int(l*Arguments['end_percent']/100)
    frames = []
    for i in range(a,b):
        frame = Image.fromarray(cv2.cvtColor(video[i], cv2.COLOR_BGR2RGB))
        if Arguments['scale_divider'] != 1:
            frame = frame.resize(
                ( na([shape(frame)[1],shape(frame)[0]]) / Arguments['scale_divider'] ).astype(int)
            )
        frames.append(frame)


def Facenet():
    """
    https://github.com/timesler/facenet-pytorch
    """
    from facenet_pytorch import MTCNN
    import torch
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    mtcnn = MTCNN(keep_all=True, device=device)

    def get_boxes(frame):
        boxes, _ = mtcnn.detect(frame)
        return boxes

    def draw_boxes(frame,boxes):
        from PIL import ImageDraw
        frame_with_boxes = frame.copy()
        draw = ImageDraw.Draw(frame_with_boxes)
        try:
            for box in boxes:
                draw.rectangle(box.tolist(), outline=(255, 0, 0), width=6)
        except:
            pass
        return na(frame_with_boxes)

    return namedtuple(
        '_',
        'get_boxes draw_boxes')(
         get_boxes, draw_boxes
    )




if __name__ == '__main__':
    
    N = Facenet()

    skip = 1
    rng = list(range(0,len(frames),skip))

    for i in rng:

        frame = frames[i]

        boxes = N.get_boxes( frame )

        frame_with_boxes = N.draw_boxes( frame, boxes )

        mci( frame_with_boxes, delay=1 )


#,b

#EOF
