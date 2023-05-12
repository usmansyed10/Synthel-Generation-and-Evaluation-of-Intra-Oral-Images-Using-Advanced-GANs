Progressive Growing GAN-PyTorch
============================
A Pytorch implementation of Progressive Growing GAN.

Requirement
----------------------------
* Argparse
* Numpy
* Matplotlib
* Pillow
* Python 3.7
* PyTorch
* TorchVision
* tqdm


Usage
----------------------------

### Training

Run the script train.py to train the network with Intra-Oral dataset.
```
$ python train.py --h    

usage: train.py [-h] [--root ROOT] [--epochs EPOCHS] [--out_res OUT_RES]
                [--resume RESUME] [--cuda]

optional arguments:
  -h, --help         show this help message and exit
  --root ROOT        directory contrains the data and outputs
  --epochs EPOCHS    training epoch number
  --out_res OUT_RES  The resolution of final output image
  --resume RESUME    continues from epoch number
  --cuda             Using GPU to train
```
#### Training Process

![training](gif)

Sample Results
----------------------------

![outputs](picture output)


