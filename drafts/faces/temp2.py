from k3.vis3 import *
from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
import pandas as pd



device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print('Running on device: {}'.format(device))

resnet = InceptionResnetV1(pretrained='vggface2').eval().to(device)



a = zeros((100,160,3),np.uint8)
a = a.transpose(2,0,1)
b = torch.from_numpy(a).float()

embeddings = resnet(
	torch.stack([b]).to(device)
).detach().cpu()

