from os import listdir
import numpy as np
import cv2
from tensorflow.keras.models import load_model
IMAGE_SIZE1 = 224
IMAGE_SIZE2 = 224



def read_image(path):
    x = cv2.imread(path, cv2.IMREAD_COLOR)
    x = cv2.resize(x, (IMAGE_SIZE1, IMAGE_SIZE2))
    x = x/255.0
    return x

def iris_centrum(file_mask):
    image_mask=file_mask
    x=[]
    y=[]
    for i in range (223):
        for j in range(223):
            if image_mask[i,j] !=0:
                x.append(i)
                y.append(j)
    yc=int(sum(x) /len(x))
    xc=int(sum(y) /len(y))
    return(xc,yc)

def iris_seg_extract(path):
    model_iris_edge = load_model('MobileNetV2_Iris_Seg_10May.h5')
    path_list=path.split('_')
    onlyfiles = listdir('./'+path_list[0]+'/test/image/')
    path_list='./'+path_list[0]+'/test/image/'
    for file in onlyfiles:
        x1 = read_image(path_list+file)
        y_pred = model_iris_edge.predict(np.expand_dims(x1, axis=0))[0]
        normalized = (y_pred[:, :, 1] - np.min(y_pred[:, :, 1])) / (np.max(y_pred[:, :, 1]) - np.min(y_pred[:, :, 1]))
        normalized = normalized * 255
        normalized = normalized > 150
        normalized = normalized * 255
        normalized = normalized.astype(np.uint8)
        croped_image = cv2.resize(normalized, (1088, 640))
        file_split = file.split('.')
        cv2.imwrite('./'+path+'/SegmentationClass/'+file_split[0]+'.png', croped_image)
def iris_seg_extract_mobile(path):
    model_iris_edge = load_model('MobileNetV2_Iris_Seg_10May.h5')
   #model_init_pupil = load_model('MobileNetV2_Pupil_total.h5')
    path_list=path.split('_')
    onlyfiles = listdir('./'+path_list[0]+'/test/image/')
    path_list='./'+path_list[0]+'/test/image/'
    for file in onlyfiles:
        x1 = read_image(path_list+file)
        y_pred = model_iris_edge.predict(np.expand_dims(x1, axis=0))[0]
        normalized = (y_pred[:, :, 1] - np.min(y_pred[:, :, 1])) / (np.max(y_pred[:, :, 1]) - np.min(y_pred[:, :, 1]))
        normalized = normalized * 255
        normalized = normalized > 150
        normalized = normalized * 255
        normalized = normalized.astype(np.uint8)
        croped_image = cv2.resize(normalized, (400, 400))
        file_split = file.split('.')
        cv2.imwrite('./' + path + '/SegmentationClass/' + file_split[0] + '.png', croped_image)
def iris_seg_extract_asia(path_in,path):
    model_iris_edge = load_model('MobileNetV2_Iris_Seg_10May.h5')
    onlyfiles = listdir('./' + path_in)
    path_list = './' + path_in + '/'
    for file in onlyfiles:
        x1 = read_image(path_list+file)
        y_pred = model_iris_edge.predict(np.expand_dims(x1, axis=0))[0]
        normalized = (y_pred[:, :, 1] - np.min(y_pred[:, :, 1])) / (np.max(y_pred[:, :, 1]) - np.min(y_pred[:, :, 1]))
        normalized = normalized * 255
        normalized = normalized > 150
        normalized = normalized * 255
        normalized = normalized.astype(np.uint8)
        croped_image = cv2.resize(normalized, (640, 480))
        file_split = file.split('.')
        cv2.imwrite('./' + path + '/SegmentationClass/' + file_split[0] + '.png', croped_image)


