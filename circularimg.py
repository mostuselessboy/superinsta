
def circularimg(filename):
   import numpy as np
   from PIL import Image, ImageDraw
   import os
   img=Image.open(filename).convert("RGB")
   npImage=np.array(img)
   h,w=img.size
   alpha = Image.new('L', img.size,0)
   draw = ImageDraw.Draw(alpha)
   draw.pieslice([0,0,h,w],0,360,fill=255)
   npAlpha=np.array(alpha)
   npImage=np.dstack((npImage,npAlpha))
   Image.fromarray(npImage).save(filename)

