import os, sys
import glob
import Image, ImageOps
import Tkinter, tkFileDialog  # file dialog widget

mp_limit = 200000.0
img_types = ('*.gif', '*.tif', '*.tiff', '*.png', '*.jpeg', '*.jpg',)  # tuple of img extensions
imgs = []

# cluge for case_insensitive globbing
def insensitive_glob(pattern):
    def either(c):
        return '[%s%s]'%(c.lower(),c.upper()) if c.isalpha() else c
    return glob.iglob(''.join(map(either,pattern)))


pic_dir = tkFileDialog.askdirectory(
    initialdir='./',
         title='Select photo directory to upload to GoogleDrive')

   
for root, subdirs, files in os.walk(pic_dir):
    print "--root--" + root
    for exts in img_types: 
        f = os.path.join(root, exts)
        #imgs.extend(glob.iglob(f))
        imgs.extend(insensitive_glob(f))

for i in imgs:
    im = Image.open(i)
    
    megapixels = im.size[0] * im.size[1]

    # resize image
    if megapixels > mp_limit:
        percentage = mp_limit / megapixels
        print i, percentage, percentage/2.0


    
