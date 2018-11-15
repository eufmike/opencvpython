# %%
from PIL import Image
# from pylab import *
import os
# import numpy as np


pil_im = Image.open('pikachu.png')

# pil_im.convert('L').save('pikachu_1.png')

im = np.array(pil_im.convert('L'))
print(im.dtype)
print(im.shape)

'''
im = np.array(pil_im.convert('L'), dtype = 'float64')
print(im.dtype)
print(im.shape)
'''
print(im.flatten())
nbr_bins = 256
imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
print(imhist.shape)
cdf = imhist.cumsum()
cdf = 255 * cdf / cdf[-1]
print(cdf.shape)
print(bins[:-1])

im2 = interp(im.flatten(),bins[:-1],cdf)



# %%
figure() 
hist(im.flatten(),128) 
show()
