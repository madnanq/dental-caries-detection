# Dental caries detection using a semi-supervised learning approach
[Adnan Qayyum](https://scholar.google.com.pk/citations?user=keWNlTIAAAAJ&hl=en), [Ahsen Tahir](https://scholar.google.com/citations?hl=en&user=LZumjfMAAAAJ), [Muhammad Atif Butt](https://scholar.google.com/citations?user=vf7PeaoAAAAJ&hl=en), Alexander Luke, Hasan Tahir Abbas, [Junaid Qadir](https://scholar.google.com/citations?user=EdPPQToAAAAJ&hl=en), Kamran Arshad, Khaled Assaleh, [Muhammad Ali Imran](https://scholar.google.co.uk/citations?user=HBQjTKIAAAAJ&hl=en) & [Qammer H. Abbasi](https://scholar.google.co.th/citations?user=Q19YO5YAAAAJ&hl=en)

[Paper](https://www.nature.com/articles/s41598-023-27808-9) Published in Scientific Reports (Springer Nature)

# Installations (for local execution with PyTorch)
## Prerequisites
1. Windows/Ubuntu
2. Anaconda Python
3. PyTorch (https://pytorch.org/get-started/locally/)
4. Albumentations (https://pypi.org/project/albumentations/), (pip install albumentations)
5. Tensorboard (https://pypi.org/project/tensorboard/), (pip install tensorboard)
6. TensorboardX (https://pypi.org/project/tensorboardX/), (pip install tensorboardX)

## Dataset 
We present a dental-caries detection dataset to train and evaluate supervised/semi-supervised methods. You can request data access by filling out this [Google Form](Google Form Link). Our labeled dataset contains 141 images.

# Training

## Data Preprocessing

-  Use 'Centroid_Augmentation.ipynb' to apply our preprocessing techniques.

## Train your model
```
python train.py --resume-training no
```

# Testing 

## Test the model on the image 

-  Use this Python script to apply pixel-level segmentation on dental image of your choice.
```
python test.py --model-path <path to saved checkpoint/weight file> --input <path to image>.
```
example: python test.py --model-path model.pth --input abc.jpg


# Citation
```
@article{qayyum2023dental,
  title={Dental caries detection using a semi-supervised learning approach},
  author={Qayyum, Adnan and Tahir, Ahsen and Butt, Muhammad Atif and Luke, Alexander and Abbas, Hasan Tahir and Qadir, Junaid and Arshad, Kamran and Assaleh, Khaled and Imran, Muhammad Ali and Abbasi, Qammer H},
  journal={Scientific Reports},
  volume={13},
  number={1},
  pages={749},
  year={2023},
  publisher={Nature Publishing Group UK London}
}
```
