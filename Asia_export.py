from pupil_export import pupil_extract_asia
from iris_edge_export import iris_edge_extract_asia
from iris_seg_export import iris_seg_extract_asia

IMAGE_SIZE1=224
IMAGE_SIZE2=224


def Asia():
    path1='CASIA-Iris-Asia_output/CASIA-distance'
    path2='CASIA-Iris-Asia_output/CASIA-Iris-Complex-Occlusion'
    path3='CASIA-Iris-Asia_output/CASIA-Iris-Complex-Off_angle'
    path_in1='CASIA-Iris-Asia/CASIA-distance/test/image'
    path_in2='CASIA-Iris-Asia/CASIA-Iris-Complex/Occlusion/test/image'
    path_in3='CASIA-Iris-Asia/CASIA-Iris-Complex/Off_angle/test/image'

    pupil_extract_asia(path_in1,path1)
    pupil_extract_asia(path_in2,path2)
    pupil_extract_asia(path_in3,path3)

    iris_edge_extract_asia(path_in1, path1)
    iris_edge_extract_asia(path_in2, path2)
    iris_edge_extract_asia(path_in3, path3)

    iris_seg_extract_asia(path_in1, path1)
    iris_seg_extract_asia(path_in2, path2)
    iris_seg_extract_asia(path_in3, path3)
