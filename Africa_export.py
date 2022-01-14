from pupil_export import pupil_extract
from iris_edge_export import iris_edge_extract
from iris_seg_export import iris_seg_extract
def Africa(path):
    pupil_extract(path)
    iris_edge_extract(path)
    iris_seg_extract(path)