import sys
import numpy as np
from PIL import Image, ImageOps

path = sys.argv[1]
ch = '#'
# Ram
#ch = '\u0930\u093E\u092E'
if len(sys.argv) > 2:
    ch = sys.argv[2]

def load_img(path):
    img = Image.open(path)
    img = ImageOps.grayscale(img)
    basewidth = 30
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    return np.array(img.resize((basewidth,hsize), Image.ANTIALIAS))

def print_img(ims, cl=250, ch='#'):
    ims = (ims < cl)
    for row in ims:
        for c in row:
            if c:
                print (ch, end=' ')
            else:
                print (' '*len(ch), end=' ')
        print ()

if __name__ == '__main__':
    ims = load_img(path)
    print_img(ims, ch=ch)

