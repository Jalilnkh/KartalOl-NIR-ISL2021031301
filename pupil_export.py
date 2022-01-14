from os import listdir
import numpy as np
import cv2
from skimage.morphology import skeletonize
from tensorflow.keras.models import load_model
IMAGE_SIZE1 = 224
IMAGE_SIZE2 = 224

def read_image(path):
    x = cv2.imread(path, cv2.IMREAD_COLOR)
    #x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
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

def pupil_extract(path):
    model_pupil = load_model('MobileNetV2_Inner_boundary_10May.h5')
    path_list=path.split('_')
    onlyfiles = listdir('./'+path_list[0]+'/test/image/')
    path_list='./'+path_list[0]+'/test/image/'
    for file in onlyfiles:
        x1 = read_image(path_list+file)
        y_pred = model_pupil.predict(np.expand_dims(x1, axis=0))[0]
        normalized = (y_pred[:, :, 1] - np.min(y_pred[:, :, 1])) / (
                            np.max(y_pred[:, :, 1]) - np.min(y_pred[:, :, 1]))
        normalized = normalized * 255
        normalized = normalized > 150
        normalized = normalized * 255
        normalized = normalized.astype(np.uint8)
        croped_image = cv2.resize(normalized, (1088, 640))
        dst = cv2.fastNlMeansDenoising(croped_image, None, 150.0, 7, 21)
        th2 = dst > 172
        # image = invert(th2)
        # This part skeletonize images
        skeleton = skeletonize(th2)

        skeleton_img = skeleton.astype(np.uint8)  # convert to an unsigned byte
        skeleton_img *= 255
        img_gray = croped_image * 0
        contours1, hierarchy = cv2.findContours(skeleton_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        max_circle = np.ndarray(shape=(2, 2), dtype=float, order='F')
        for shape_ob in contours1:
            if shape_ob.shape[0] > max_circle.shape[0]:
                max_circle = shape_ob
        flag = 0
        for shape_ob in contours1:
            if shape_ob.shape[0] > max_circle.shape[0]:
                max_circle = shape_ob
                flag = 1
        if flag:
            img_gray = cv2.drawContours(img_gray, max_circle, -1, (255, 255, 255), 1)

        else:
            img_gray = skeleton_img
        file_split = file.split('.')
        cv2.imwrite('./'+path+'/Inner_Boundary/'+file_split[0]+'.png', img_gray)

def pupil_extract_mobile(path):
    model_pupil = load_model('MobileNetV2_Inner_boundary_10May.h5')
    path_list=path.split('_')
    onlyfiles = listdir('./'+path_list[0]+'/test/image/')
    path_list='./'+path_list[0]+'/test/image/'

    for file in onlyfiles:
        x1 = read_image(path_list+file)
        y_pred = model_pupil.predict(np.expand_dims(x1, axis=0))[0]
        normalized = (y_pred[:, :, 1] - np.min(y_pred[:, :, 1])) / (
                np.max(y_pred[:, :, 1]) - np.min(y_pred[:, :, 1]))
        normalized = normalized * 255
        normalized = normalized > 150
        normalized = normalized * 255
        normalized = normalized.astype(np.uint8)
        croped_image = cv2.resize(normalized, (400, 400))
        dst = cv2.fastNlMeansDenoising(croped_image, None, 150.0, 7, 21)
        th2 = dst > 172
        # image = invert(th2)
        # This part skeletonize images
        skeleton = skeletonize(th2)

        skeleton_img = skeleton.astype(np.uint8)  # convert to an unsigned byte
        skeleton_img *= 255
        img_gray = croped_image * 0
        contours1, hierarchy = cv2.findContours(skeleton_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        max_circle = np.ndarray(shape=(2, 2), dtype=float, order='F')
        for shape_ob in contours1:
            if shape_ob.shape[0] > max_circle.shape[0]:
                max_circle = shape_ob
        flag = 0
        for shape_ob in contours1:
            if shape_ob.shape[0] > max_circle.shape[0]:
                max_circle = shape_ob
                flag = 1
        if flag:
            img_gray = cv2.drawContours(img_gray, max_circle, -1, (255, 255, 255), 1)

        else:
            img_gray = skeleton_img
        file_split = file.split('.')
        cv2.imwrite('./'+path+'/Inner_Boundary/'+file_split[0]+'.png', img_gray)

def pupil_extract_asia(path_in,path):
    model_pupil = load_model('MobileNetV2_Inner_boundary_10May.h5')
    onlyfiles = listdir('./'+path_in)
    path_list='./'+path_in+'/'
    for file in onlyfiles:
        x1 = read_image(path_list+file)
        y_pred = model_pupil.predict(np.expand_dims(x1, axis=0))[0]
        normalized = (y_pred[:, :, 1] - np.min(y_pred[:, :, 1])) / (
                np.max(y_pred[:, :, 1]) - np.min(y_pred[:, :, 1]))
        normalized = normalized * 255
        normalized = normalized > 150
        normalized = normalized * 255
        normalized = normalized.astype(np.uint8)
        croped_image = cv2.resize(normalized, (640, 480))
        dst = cv2.fastNlMeansDenoising(croped_image, None, 150.0, 7, 21)
        th2 = dst > 172
        # image = invert(th2)
        # This part skeletonize images
        skeleton = skeletonize(th2)

        skeleton_img = skeleton.astype(np.uint8)  # convert to an unsigned byte
        skeleton_img *= 255
        img_gray = croped_image * 0
        contours1, hierarchy = cv2.findContours(skeleton_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        max_circle = np.ndarray(shape=(2, 2), dtype=float, order='F')
        for shape_ob in contours1:
            if shape_ob.shape[0] > max_circle.shape[0]:
                max_circle = shape_ob
        flag = 0
        for shape_ob in contours1:
            if shape_ob.shape[0] > max_circle.shape[0]:
                max_circle = shape_ob
                flag = 1
        if flag:
            img_gray = cv2.drawContours(img_gray, max_circle, -1, (255, 255, 255), 1)

        else:
            img_gray = skeleton_img
        file_split = file.split('.')
        cv2.imwrite('./'+path+'/Inner_Boundary/'+file_split[0]+'.png', img_gray)

