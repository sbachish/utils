import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from scipy import misc, ndimage, io
from skimage import color, measure

import pymorph as MM



def crp_rsz_bin(img_file, crop_size=150, resize_size=40, bin_k=60, show_plot=True):

    img = Image.open(img_file)

    plt.subplot(141)
    plt.imshow(img)

    width, height = img.size   # Get dimensions
    left = (width - crop_size)/2
    top = (height - crop_size)/2
    right = (width + crop_size)/2
    bottom = (height + crop_size)/2
    img = img.crop((left, top, right, bottom))

    plt.subplot(142)
    plt.imshow(img)

    img = img.resize((resize_size,resize_size), Image.ANTIALIAS)
    img.save('_img.jpg')
    img= misc.imread('_img.jpg', flatten=1)

    plt.subplot(143)
    plt.imshow(img)

    img = img.astype(np.uint8)
    img = MM.binary(img,k=bin_k)
    img = np.asarray(img, dtype='int')

    plt.subplot(144)
    plt.imshow(img)

    if show_plot:
        plt.show()
    return img

#-------------------------------------------------
crp_rsz_bin('100023.jpg')
