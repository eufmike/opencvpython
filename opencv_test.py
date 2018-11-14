# %%
from PIL import Image
import os
pil_im = Image.open('pikachu.png')

pil_im.convert('L').save('pikachu_1.png')

