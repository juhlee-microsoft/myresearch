import os
import shutil
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Needed to display matplotlib plots in Jupyter
%matplotlib inline

imgdir = 'gear_images' # Folder containing extracted images

# Create a figure to display the images
fig = plt.figure(figsize=(12, 16))

# loop recursively through the folders
dir_num = 0
for root, folders, filenames in os.walk(imgdir):
    for folder in folders:
        # in each folder, get the first file
        imgFile = os.listdir(os.path.join(root,folder))[0]
        filePath = os.path.join(root,folder,imgFile)
        # Open it and add it to the figure (in a 4-row grid)
        img = Image.open(filePath)
        
        a=fig.add_subplot(12,2,dir_num + 1)    
        plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=1)
        imgplot = plt.imshow(img)
        
        # Add the folder name (the class of the image)
        a.set_title(folder)
        dir_num = dir_num + 1
        
        img_arry = np.array(img)

        size = 128, 128
        # Create new image, img2 with size 128x128 RGB
        img2 = Image.new('RGB', size, 'white')
        
        # Resizing img to thumbnail size
        img.thumbnail(size, Image.ANTIALIAS)
        
        # Pasting img to img2
        img2.paste(img)
        
        a=fig.add_subplot(12,2,dir_num + 1)
        imgplot = plt.imshow(img2)
        
        dir_num = dir_num + 1

plt.show()