#,a
from k3.utils3 import *


def F():
    """
    https://github.com/timesler/facenet-pytorch
    """
    from facenet_pytorch import MTCNN
    import torch
    import numpy as np
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    mtcnn = MTCNN(keep_all=True, device=device)
    
    def process_frame(frame):
        boxes, _ = mtcnn.detect(frame)
        return boxes

    return namedtuple('FaceNet_object', 'process_frame')(process_frame)


#,b

#EOF
