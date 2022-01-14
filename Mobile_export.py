from pupil_export import pupil_extract_mobile
from iris_edge_export import iris_edge_extract_mobile
from iris_seg_export import iris_seg_extract_mobile

def Mobile(path):
    pupil_extract_mobile(path)
    iris_edge_extract_mobile(path)
    iris_seg_extract_mobile(path)

