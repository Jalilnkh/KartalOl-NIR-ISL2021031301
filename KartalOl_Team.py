#!/usr/bin/env python 

import os
import sys
import argparse
from Africa_export import Africa
from Asia_export import Asia
from Mobile_export import  Mobile
from argparse import RawTextHelpFormatter


def argument_parser():
    parser = argparse.ArgumentParser(description=__doc__, prog='cryoem_scorings', formatter_class=RawTextHelpFormatter)
    parser.add_argument("-f", "--filename", required=True, dest="file",
                        help="Input file. Sequence alignment in proper format.")
    args = parser.parse_args()
    infile = args.file
    return infile

def main():
    key=argument_parser()
    print(key)
    if key == 'Africa':
        cmd="rm -f -r CASIA-Iris-Africa_output"
        path="CASIA-Iris-Africa_output"
        os.system(cmd)
        os.mkdir('CASIA-Iris-Africa_output')
        os.mkdir('CASIA-Iris-Africa_output/Inner_Boundary')
        os.mkdir('CASIA-Iris-Africa_output/Outer_Boundary')
        os.mkdir('CASIA-Iris-Africa_output/SegmentationClass')
        Africa(path)

    if key == 'Asia':
        cmd = "rm -f -r CASIA-Iris-Asia_output"
        os.system(cmd)
        os.mkdir('CASIA-Iris-Asia_output')
        os.mkdir('CASIA-Iris-Asia_output/CASIA-distance')
        os.mkdir('CASIA-Iris-Asia_output/CASIA-distance/Inner_Boundary')
        os.mkdir('CASIA-Iris-Asia_output/CASIA-distance/Outer_Boundary')
        os.mkdir('CASIA-Iris-Asia_output/CASIA-distance/SegmentationClass')
        os.mkdir('CASIA-Iris-Asia_output/CASIA-Iris-Complex-Occlusion')
        os.mkdir('CASIA-Iris-Asia_output/CASIA-Iris-Complex-Occlusion/Inner_Boundary')
        os.mkdir('CASIA-Iris-Asia_output/CASIA-Iris-Complex-Occlusion/Outer_Boundary')
        os.mkdir('CASIA-Iris-Asia_output/CASIA-Iris-Complex-Occlusion/SegmentationClass')
        os.mkdir('CASIA-Iris-Asia_output/CASIA-Iris-Complex-Off_angle')
        os.mkdir('CASIA-Iris-Asia_output/CASIA-Iris-Complex-Off_angle/Inner_Boundary')
        os.mkdir('CASIA-Iris-Asia_output/CASIA-Iris-Complex-Off_angle/Outer_Boundary')
        os.mkdir('CASIA-Iris-Asia_output/CASIA-Iris-Complex-Off_angle/SegmentationClass')
        path="CASIA-Iris-Asia_output"
        Asia()
    if key == 'Mobile':
        cmd = "rm -f -r CASIA-Iris-Mobile-V1.0_output"
        os.system(cmd)
        os.mkdir('CASIA-Iris-Mobile-V1.0_output')
        os.mkdir('CASIA-Iris-Mobile-V1.0_output/Inner_Boundary')
        os.mkdir('CASIA-Iris-Mobile-V1.0_output/Outer_Boundary')
        os.mkdir('CASIA-Iris-Mobile-V1.0_output/SegmentationClass')
        path="CASIA-Iris-Mobile-V1.0_output"
        Mobile(path)

if __name__ == "__main__":
    main()