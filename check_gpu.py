import sys 
import torch
import cv2
print('cuda available:',torch.cuda.is_available())
print('GPU count:',torch.cuda.device_count())
print('Python version:',sys.version)
print('Pytorch Version:',torch.__version__)
print('openCV:',cv2.__version__)
print(torch.tensor([0.1, 0.2], device=torch.device('cuda:0')))
# tensor([0.1000, 0.2000], device='cuda:0')
