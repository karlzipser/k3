# https://github.com/pgtgrly/Convolution-Deconvolution-Network-Pytorch/blob/master/Neural_Network_Class.py
from k3.utils3 import *
import torch
import torch.nn as nn
from torch.autograd import Variable
class conv_deconv(nn.Module):

    def __init__(self):
        super(conv_deconv,self).__init__()

        self.conv1=nn.Conv2d(in_channels=3,out_channels=16, kernel_size=4,stride=1, padding=0)
        nn.init.xavier_uniform(self.conv1.weight) #Xaviers Initialisation
        self.swish1= nn.ReLU()

        self.maxpool1= nn.MaxPool2d(kernel_size=2,return_indices=True)

        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=5)
        nn.init.xavier_uniform(self.conv2.weight)
        self.swish2 = nn.ReLU()

        self.maxpool2 = nn.MaxPool2d(kernel_size=2,return_indices=True)

        self.conv3 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3)
        nn.init.xavier_uniform(self.conv3.weight)
        self.swish3 = nn.ReLU()

        self.deconv1=nn.ConvTranspose2d(in_channels=64,out_channels=32,kernel_size=3)
        nn.init.xavier_uniform(self.deconv1.weight)
        self.swish4=nn.ReLU()

        self.maxunpool1=nn.MaxUnpool2d(kernel_size=2)

        self.deconv2=nn.ConvTranspose2d(in_channels=32,out_channels=16,kernel_size=5)
        nn.init.xavier_uniform(self.deconv2.weight)
        self.swish5=nn.ReLU()

        self.maxunpool2=nn.MaxUnpool2d(kernel_size=2)

        self.deconv3=nn.ConvTranspose2d(in_channels=16,out_channels=3,kernel_size=4)
        nn.init.xavier_uniform(self.deconv3.weight)
        self.swish6=nn.ReLU()

    def forward(self,x):
        out=self.conv1(x)
        out=self.swish1(out)
        size1 = out.size()
        out,indices1=self.maxpool1(out)
        out=self.conv2(out)
        out=self.swish2(out)
        size2 = out.size()
        out,indices2=self.maxpool2(out)
        out=self.conv3(out)
        out=self.swish3(out)

        out=self.deconv1(out)
        out=self.swish4(out)
        out=self.maxunpool1(out,indices2,size2)
        out=self.deconv2(out)
        out=self.swish5(out)
        out=self.maxunpool2(out,indices1,size1)
        out=self.deconv3(out)
        out=self.swish6(out)
        return(out)

if __name__ == '__main__':
    C = conv_deconv()
    #x = torch.DoubleTensor(zeros((16,3,30,30))).float()
    x = torch.DoubleTensor(zeros((16,3,41,23))).float()
    y = C.forward(x)
    print y.size()

#EOF