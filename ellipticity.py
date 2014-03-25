import numpy as np

from PIL import Image
from scipy import misc, ndimage, io
from skimage import color, measure


import pymorph as MM



def ellipticity(imj_obj, crop_size=None, resize_size=None):
  if 
  
  if
  
  if 
  
  img = Image.open(img_dir+'data/sample_train/'+img_file)
  width, height = img.size   # Get dimensions
  left = (width - crop_size)/2
  top = (height - crop_size)/2
  right = (width + crop_size)/2
  bottom = (height + crop_size)/2

  img = img.crop((left, top, right, bottom))





  return
