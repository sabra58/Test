import glob, os, sys
from PIL import Image

folder = '/home/sabra/Downloads/Images/a'

for filepath in glob.iglob(os.path.join(folder, '*.jpg')):
    image = Image.open(filepath).convert('RGB').convert('L')
    new_filepath = os.path.splitext(filepath)[0] + '.bmp'
    image.save(new_filepath)

