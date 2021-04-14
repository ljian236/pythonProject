import torch
from torch import nn
from torch.autograd import Variable
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

#Hyper Parameters
EPOCH =1 #train the traning data n times, to save time, we just train 1 epoch
BATCH_SIZE = 64
TIME_STEP=28 #rnn time step / image height
INPUT_SIZE=28 #rnn input size / image width
LR=0.01 #learning rate
DOWNLOAD_MNIST=True # set to True if haven't download the data

train_data=dsets.MNIST(root='./mnist', train=True, transforms=transforms.ToTensor(), download=DOWNLOAD_MNIST)
train_loader=torch.utils.data.DataLoader()

test_data=


