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
    import torch
    from facenet_pytorch import InceptionResnetV1
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    Arguments = get_Arguments(
        Defaults={
            'src':REQUIRED,
            'start_percent':0,
            'end_percent':100,
            'scale_divider':1,
            'save_faces':True,
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

    skip = 4
    rng = list(range(0,len(frames),skip))

    clp('resized frame shape =',shape(frames[0]),'`wbb')


    P = Percent(
        'Detecting faces...',
        '\tdisplaying:',
        '\tdisplayed:'
    )
    
    frame_size = shape(frames[0])
    width = frame_size[1]
    height = frame_size[0]
    larger_frame = zeros((frame_size[0]*2,width*2,3),np.uint8) + 127

    resnet = InceptionResnetV1(pretrained='vggface2').eval().to(device)
    
    data = []

    for i in rng:

        frame = na(frames[i])

        boxes, probs, landmarks = N.get_boxes( frame )

        P.show(i,len(rng))

        larger_frame[height//2:int(1.5*height),width//2:int(1.5*width),:] = frame

        mci( frame, title='frame',delay=1 )

        if boxes is not None and landmarks is not None:
            ctr = 0
            for box, landmark in zip(boxes, landmarks):
                x0,x1,y0,y1 = intr(box[0]),intr(box[2]),intr(box[1]),intr(box[3])
                dx = x1 - x0
                dy = y1 - y0
                if False:
                    plot((x0,x1),(y0,y0),'r')
                    plot((x0,x1),(y1,y1),'r')
                    plot((x0,x0),(y0,y1),'r')
                    plot((x1,x1),(y0,y1),'r')
                    plt.scatter(*np.meshgrid(box[[0, 2]], box[[1, 3]]))
                    plt.scatter(landmark[:, 0], landmark[:, 1], s=8)

                try:
                    face = larger_frame[height//2+y0-dy//4:height//2+y1+dy//4,width//2+x0-dx//4:width//2+x1+dx//4,:]
                    mci(face,title=str(6+ctr),delay=1)

                    embeddings = [0]
                    face_ = face.transpose(2,0,1).copy()
                    
                    a = face.copy()
                    a = a.transpose(2,0,1)
                    b = torch.from_numpy(a).float()
                    try:
                        embeddings = resnet(
                            torch.stack([b]).to(device)
                        ).detach().cpu()

                        data.append(
                            {
                                'x0':x0,
                                'x0':x1,
                                'y0':y0,
                                'y1':y1,
                                'face':face.copy(),
                                'frame':i,
                                'file':Arguments['src'],
                                'landmark':landmark,
                                'embedding':embeddings[0],
                            }
                        )
                    except:
                        cr('failure')
                    #mi(data[-1]['face'])
                except:
                    cg('failure')
                ctr += 1
        spause()

    P.show()

    if Arguments['save_faces']:
        soD(data,'data')



if True:
    o = loD('data')
    for a in o:
        mci(a['face'],delay=33)
        figure(1);clf()
        plot(a['embedding'])
        spause()

    mi(o[0]['face'],100)
    for i in rlen(o):
        figure(2);clf();plt_square()
        plot(o[0]['embedding'],o[i]['embedding'],'.')
        mi(o[i]['face'],101)
        spause()


#,b

#EOF
