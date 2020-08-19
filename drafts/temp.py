from k3.vis3 import *
from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
#from torch.utils.data import DataLoader
#from torchvision import datasets
import pandas as pd


#workers = 0 if os.name == 'nt' else 4

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print('Running on device: {}'.format(device))

mtcnn = MTCNN(
    image_size=160, margin=0, min_face_size=20,
    thresholds=[0.6, 0.7, 0.7], factor=0.709, post_process=True,
    device=device
)

resnet = InceptionResnetV1(pretrained='vggface2').eval().to(device)

aligned = []
files = sggo('/Volumes/pn disk 1/temp/*.png')
for f in files:
	print(f)
	img = zimread(f)
	x_aligned, prob = mtcnn(img, return_prob=True)
	if x_aligned is None:
		x_aligned = 0*aligned[0]
	aligned.append(x_aligned)



embeddings = resnet(
	torch.stack(aligned).to(device)
).detach().cpu()

la = len(aligned)
q = zeros((la,la))
for i in range(la):
	for j in range(la):
		e = embeddings[i].numpy()
		f = embeddings[j].numpy()
		q[i,j] = np.sum((e*f))

raw_enter()

for a in aligned:
	if a is not None:
		b = a.numpy().transpose(1,2,0)
		mci(z55(b),delay=33,title='all')

raw_enter()

for i in range(la):
	if q[100,i] < .1:
		mci(z55(aligned[i].numpy().transpose(1,2,0)),delay=500,title='low')

raw_enter()

for i in range(la):
	if q[100,i] > 0.4:
		mci(z55(aligned[i].numpy().transpose(1,2,0)),delay=500,title='high')

