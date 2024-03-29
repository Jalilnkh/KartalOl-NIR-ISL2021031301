# KartalOl: Transfer learning using deep neural network for iris segmentation and localization: New dataset for iris segmentation 

Read about the paper in the following link:

   https://arxiv.org/abs/2112.05236 

Abstarct:


Iris segmentation and localization in unconstrained environments is challenging due to long distances, illumination variations, limited user cooperation, and moving subjects. To address this problem, we present a U-Net with a pre-trained MobileNetV2 deep neural network method. We employ the pre-trained weights given with MobileNetV2 for the ImageNet dataset and fine-tune it on the iris recognition and localization domain. Further, we have introduced a new dataset, called KaratolOl, to better evaluate detectors in iris recognition scenarios. To provide domain adaptation, we fine-tune the MobileNetV2 model on the provided data for NIR-ISL 2021 from the CASIA-Iris-Asia, CASIA-Iris-M1, and CASIA-Iris-Africa and our dataset. We also augment the data by performing left-right flips, rotation, zoom, and brightness. We chose the binarization threshold for the binary masks by iterating over the images in the provided dataset. The proposed method is tested and trained in CASIA-Iris-Asia, CASIA-Iris-M1, CASIA-Iris-Africa, along the KaratolOl dataset. The experimental results highlight that our method surpasses state-of-the-art methods on mobile-based benchmarks. The codes and evaluation results are publicly available at https://github.com/Jalilnkh/KartalOl-NIR-ISL2021031301. [1], [2]


This code was implemented by KartalOl Team, contains Farhang Jaryani, Jalil Nourmohammadi Khiarak, Seyed Naeim Moafinejad, Samaneh Salehi Nasab, Yasin Amini, and Morteza Noshad.
The code is contains  9 python files and 3 save model files (.h5), 3 output folders (CASIA-Iris-Africa_output, CASIA-Iris-Asia_output, and CASIA-Iris-Mobile-V1.0_output).

### To run the code do as follows:

#### Requirement:

1- Keras

2- Numpy

3- Python 3 

4- Tensorflow version 2 or new one

5- Cv2 (Opencv- python)

6- skimage.morphology import skeletonize

6- Ubuntu 18

7- the most important part is trained weights. Because trainingset is not possible to share I will uplaod weights in the Google drive you could find it in the following links:

   7-1: Trained weights for Outter boundary https://drive.google.com/file/d/1WrOcJNUmM1anyg-iyOqExtbZwaXcoqNR/view?usp=sharing
   
   7-2: Trained weights for Inner boundary https://drive.google.com/file/d/1tqtyFs0eu7RsCkl9SyWdwdzLaE4pr5gW/view?usp=sharing 
   
   7-3: Trained weights for Iris segmentation https://drive.google.com/file/d/1kJZcUX5lDqc7BiU7jSj0GTZuZwepbns8/view?usp=sharing 

After downloading the wieghts you should put them in the main directory:

       ~/KartalOl-NIR-ISL2021031301/
      

In order to run each categories, you are supposed to mention the name of category after -f as follows.:
Open a terminal in the current directory and run:

        1- python3 KartalOl_Team.py -f Africa

Output: The output folders will be generated automatically. CASIA-Iris-Africa_output would be the output of the run code.

        2- python3 KartalOl_Team.py -f Asia

Output: The output folders will be generated automatically. CASIA-Iris-Asia_output would be the output of the run code.

        3- python3 KartalOl_Team.py -f Mobile

Output: The output folders will be generated automatically. CASIA-Iris-Mobile-V1.0_output would be the output of the run code.


PS: the outputs for all given test files are attached. 


### Reference:

Please cite the following papers if you are using the code:

[1] Jalil Nourmohammadi Khiarak*, et al., "KartalOl: Transfer learning using deep neural network for iris segmentation and localization: New dataset for iris segmentation", 2021, https://arxiv.org/abs/2112.05236.

[2] Wang, Caiyong, et al. "NIR iris challenge evaluation in non-cooperative environments: Segmentation and localization." 2021 IEEE International Joint Conference on Biometrics (IJCB). IEEE, 2021.

