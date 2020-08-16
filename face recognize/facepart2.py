import cv2
from os import listdir
from os.path import isfile, join
import numpy as np

data_path = 'C:/Users/HP/Desktop/image/'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
Training_Data, Labels = [], []
for i, files in enumerate(onlyfiles):
    image_path = data_path+onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(np.asarray(i, dtype=np.int32))
# pip install opencv-contrib-python(for lbphfacerecognizer)
model = cv2.face.LBPHFaceRecognizer_create()
model.train(np.asarray(Training_Data), np.asarray(Labels))
print("training data is completed")
