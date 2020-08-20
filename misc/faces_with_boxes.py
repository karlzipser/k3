#,a

"""
pip install mmcv

https://github.com/timesler/facenet-pytorch
pip install facenet-pytorch

"""

from k3.vis3 import *


def Facenet():

    from facenet_pytorch import MTCNN
    import torch
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    mtcnn = MTCNN(keep_all=True, device=device)

    def get_boxes(frame):
        boxes, probs, landmarks = mtcnn.detect(frame, landmarks=True)
        #boxes, _ = mtcnn.detect(frame)
        return boxes, probs, landmarks

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

    Arguments = get_Arguments(
        Defaults={
            'src':REQUIRED,
            'start_percent':0,
            'end_percent':100,
            'scale_divider':1,
        }
    )

    kprint(Arguments,'main')

    if 'frames' not in locals():

        from PIL import Image
        import mmcv
        video = mmcv.VideoReader(Arguments['src'])
        l = len(video)
        a = int(l*Arguments['start_percent']/100)
        b = int(l*Arguments['end_percent']/100)
        clp('frame range =',a,'to',b,'within',l,'`wbb')
        frames = []

        P = Percent(
            d2s('initial frame shape =',shape(video[0])),
            '\tloading:',
            '\tloaded:'
        )

        for i in range(a,b):
            P.show(i-a,b-a)
            frame = Image.fromarray(cv2.cvtColor(video[i], cv2.COLOR_BGR2RGB))

            if Arguments['scale_divider'] != 1:
                frame = frame.resize(
                    ( na([shape(frame)[1],shape(frame)[0]]) / Arguments['scale_divider'] ).astype(int)
                )
            frames.append(frame)
        P.show()


    N = Facenet()

    skip = 1
    rng = list(range(0,len(frames),skip))

    clp('resized frame shape =',shape(frames[0]),'`wbb')


    P = Percent(
        'Detecting faces...',
        '\tdisplaying:',
        '\tdisplayed:'
    )
    
    for i in rng:

        frame = frames[i]

        boxes, probs, landmarks = N.get_boxes( frame )

        frame_with_boxes = N.draw_boxes( frame, boxes )

        #mci( frame_with_boxes, delay=1 )

        P.show(i,len(rng))

        figure('matplotlib')
        mi(frame,5)
        if boxes is not None and landmarks is not None:
            for box, landmark in zip(boxes, landmarks):
                x0,x1,y0,y1 = intr(box[0]),intr(box[2]),intr(box[1]),intr(box[3])
                
                plot((x0,x1),(y0,y0),'r')
                plot((x0,x1),(y1,y1),'r')
                plot((x0,x0),(y0,y1),'r')
                plot((x1,x1),(y0,y1),'r')

                plt.scatter(*np.meshgrid(box[[0, 2]], box[[1, 3]]))
                plt.scatter(landmark[:, 0], landmark[:, 1], s=8)

                try:
                    mi(z55(na(frame)[y0:y1,x0:x1,:]),6)
                except:
                    pass
        spause()


    P.show()







#,b

#EOF
