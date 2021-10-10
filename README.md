# KartalOl-NIR-ISL2021031301
Iris segmentation and localization in unconstrained environments is challenging due to long distances, illumination variations, limited user cooperation, and moving subjects. To address this problem, we present a U-Net with a pre-trained MobileNetV2 deep neural network method. We employ the pre-trained weights given with MobileNetV2 for the ImageNet dataset and fine-tune it on the iris recognition and localization domain. Further, we have introduced a new dataset, called KaratolOl, to better evaluate detectors in iris recognition scenarios. To provide domain adaptation, we fine-tune the MobileNetV2 model on the provided data for NIR-ISL 2021 from the CASIA-Iris-Asia, CASIA-Iris-M1, and CASIA-Iris-Africa and our dataset. We also augment the data by performing left-right flips, rotation, zoom, and brightness. We chose the binarization threshold for the binary masks by iterating over the images in the provided dataset. The proposed method is tested and trained in CASIA-Iris-Asia, CASIA-Iris-M1, CASIA-Iris-Africa, along the KaratolOl dataset. The experimental results highlight that our method surpasses state-of-the-art methods on mobile-based benchmarks. The codes and evaluation results are publicly available at https://github.com/Jalilnkh/KartalOl-NIR-ISL2021031301 .
