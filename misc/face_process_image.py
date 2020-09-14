from k3 import *
from k3.utils.torch_.facenet import *

Arguments = get_Arguments(
    Defaults={
        'src':REQUIRED,
        'save_faces':True,
        'show_boxes':True,
    }
)

"""
pip install mmcv

https://github.com/timesler/facenet-pytorch
pip install facenet-pytorch

"""

import torch
from facenet_pytorch import InceptionResnetV1

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

FN = Facenet()
RN = InceptionResnetV1(pretrained='vggface2').eval().to(device)




def get_face_embedding_data(frame,boxes,landmarks,RN):

    
    frame_size = shape(frame)
    width = frame_size[1]
    height = frame_size[0]
    larger_frame = zeros((frame_size[0]*2,width*2,3),np.uint8) + 127
    larger_frame[
        height//2:int(1.5*height),
        width//2:int(1.5*width),
        :] = frame

    #mci( frame, title='frame',delay=1 )

    mi(frame,0)

    if boxes is not None and landmarks is not None:
        ctr = 0
        data = []
        for box, landmark in zip(boxes, landmarks):
            x0,x1,y0,y1 = \
                intr(box[0]),intr(box[2]),intr(box[1]),intr(box[3])
            dx = x1 - x0
            dy = y1 - y0
            if Arguments['show_boxes']:
                #mi(frame,0)
                figure(0)
                plot((x0,x1),(y0,y0),'r')
                plot((x0,x1),(y1,y1),'r')
                plot((x0,x0),(y0,y1),'r')
                plot((x1,x1),(y0,y1),'r')
                #plt.scatter(*np.meshgrid(box[[0, 2]], box[[1, 3]]))
                #plt.scatter(landmark[:, 0], landmark[:, 1], s=8)
                cx = (x0+x1)//2
                cy = (y0+y1)//2
                dmax = max(dx,dy)

            if True:#try:
                if False:
                    face = larger_frame[
                                height//2+y0-dy//4:height//2+y1+dy//4,
                                width//2+x0-dx//4:width//2+x1+dx//4,
                                :
                            ].copy()

                face = larger_frame[
                            height//2+cy-dmax//2:height//2+cy+dmax//2,
                            width//2+cx-dmax//2:width//2+cx+dmax//2,
                            :
                        ].copy()

                #mci(face,title=str(6+ctr),delay=1)

                #embeddings = [0]
                
                a = face.copy()
                
                a = cv2.resize(a, dsize=(160,160))
                mci(a,title=d2s('resized',ctr))
                #cg(shape(a),r=1)
                a = a.transpose(2,0,1)
                #a = a.transpose(2,1,0)
                #cg(shape(a),r=1)
                b = torch.from_numpy(a).float()
                #cb(b.size(),r=1)
                c = torch.stack([b]).to(device)
                cm(c.size())
                if True:#try:
                    embeddings = RN(
                        c,#torch.stack([b]).to(device)
                    ).detach().cpu()

                    data.append(
                        {
                            'x0':x0,
                            'x0':x1,
                            'y0':y0,
                            'y1':y1,
                            'face':face.copy(),
                            'file':Arguments['src'],
                            'landmark':landmark,
                            'embedding':embeddings[0],
                        }
                    )
                else:#except:
                    cr('failure')

            else:#except:
                cg('failure')
            ctr += 1
    spause()
    #raw_enter()
    CA()
    return data


paths = get_list_of_image_files_recursively('Pictures')   

data = []
timer = Timer(60)

for p in paths:
    p = 'Pictures/'+p.replace('Pictures/','') 
    try:
        frame = zimread(p)

        boxes, probs, landmarks = FN.get_boxes( frame )

        data += get_face_embedding_data(frame,boxes,landmarks,RN)

        if Arguments['save_faces'] and timer.check():
            timer.reset()
            soD(data,'data')
    except KeyboardInterrupt:
        cE('*** KeyboardInterrupt ***')
        sys.exit()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        pd2s(exc_type,file_name,exc_tb.tb_lineno) 

if Arguments['save_faces']:
    soD(data,'data')

if False:
    o = loD('data')
    for a in o:
        mci(a['face'],delay=33)
        figure(1);clf()
        plot(a['embedding'])
        spause()

    mi(o[0]['face'],100)
    figure(2);clf();plt_square()
    for i in rlen(o):
        figure(2)#;clf();plt_square()
        plot(o[0]['embedding'],o[i]['embedding'],'.')
        mi(o[i]['face'],101)
        spause()

if False:
    o = loD('data')
    r = zeros((len(o),len(o)))
    P = Percent()
    for i in rlen(o):
        P.show(i,len(o))
        a = o[i]['embedding']
        for j in rlen(o):
            b = o[j]['embedding']
            r[i][j] = np.corrcoef(a,b)[0,1]
    mi(r)

    rng = list(rlen(r))
    random.shuffle(rng)
    for i in rng:#rlen(r):#i = 100
        s = np.argsort(r[i])
        mi(o[i]['face'],1);spause()
        for j in range(len(s)-1,len(s)-10,-1):
            c = r[i][s[j]]
            if c < 0.97 or c > 0.99:
                pass
            else:
                print(i,r[i][s[j]])
                mi(o[s[j]]['face'],2);spause()
                time.sleep(1)



#,b

#EOF
