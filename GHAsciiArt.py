''' Load an image from file and print as ASCII art to the screen! '''
import numpy as np
from numpy.core.fromnumeric import size
from numpy.ma.core import where
import pygame as pg
from PIL import Image
   
## Pre-calculated values:

# Dimensions of a single, fixed-width character:
# (determined for Courier New: cour.ttf)
char_width = 12
char_height = 20
char_hw_ratio = char_height / char_width

# A list of characters that you can use in your ASCII art...
characters = ['M', 'W', 'Q', 'B', 'E', 'R', 'N', '@', 'H', 'q', 'p', 'g', 'K', 'A', '#', 'm', 'b', '8', '0', 'd', 'X', 'D', 'G', 'F', 'P', 'e', 'h', 'U', '9', '6', 'k', 'Z', '%', 'S', '4', 'O', 'x', 'y', 'T', '5', 'w', 'f', 'a', 'V', 's',
                '2', 'L', '$', 'Y', '&', 'n', '3', 'C', 'J', 'u', 'o', 'z', 'I', 'j', 'v', 'c', 'r', 't', 'l', 'i', '1', '=', '?', '7', '>', '<', ']', '[', '(', ')', '+', '*', ';', '}', '{', ':', '/', '\\', '!', '|', '_', ',', '^', '-', '~', '.', ' ']
n_characters = len(characters)

# ... and the corresponding grayscale values
grayscale = np.array([217.56944444, 218.82291667, 219.89236111, 220.19444444,
                      222.14583333, 222.94097222, 223.0625, 223.17361111,
                      223.22222222, 223.23958333, 223.45486111, 223.60416667,
                      224.05208333, 224.09722222, 224.33333333, 225.25,
                      225.59722222, 225.62152778, 225.91666667, 225.96180556,
                      226.10763889, 226.74305556, 226.80208333, 227.04861111,
                      227.42361111, 228.45833333, 228.61458333, 228.73958333,
                      228.76736111, 228.80555556, 228.8125, 228.90625,
                      228.98611111, 229.06597222, 229.28472222, 229.61805556,
                      229.96527778, 230.07291667, 230.17361111, 230.21875,
                      230.60416667, 230.62847222, 230.84375, 231.03472222,
                      231.05555556, 231.46875, 231.55555556, 231.9375,
                      232.04861111, 232.07291667, 232.64583333, 232.68055556,
                      233.16319444, 233.53472222, 233.70138889, 234.20833333,
                      234.40625, 234.76388889, 234.93055556, 235.30208333,
                      235.36805556, 235.44791667, 235.5, 236.53472222,
                      237.32986111, 237.67361111, 237.70138889, 238.61458333,
                      238.61805556, 238.78125, 238.78472222, 238.79166667,
                      238.98611111, 239.07638889, 239.08680556, 239.97569444,
                      240.32291667, 240.78125, 241.50694444, 241.57291667,
                      242.25694444, 243.13194444, 243.18055556, 243.31944444,
                      244.30208333, 244.61805556, 245.03819444, 246.62847222,
                      247.58333333, 247.60763889, 248.62847222, 255.0])



def getAverage(image):
    # get image as numpy array
    im = np.array(image)
    # get shape
    w,h = im.shape
    # get average
    return np.average(im.reshape(w*h))

#50 ##70
def get_char_for_value(val,min_val,max_val,char_list,char_grayscale):#
    a = (max(char_grayscale) - min(char_grayscale))/(max_val - min_val)*(val - min_val) + min(char_grayscale)
    a = char_grayscale-a
    b = np.where(a>=0)[0][0]
  
    ch = char_list[b]
  
    return ch

def get_pixel_arrays(img: pg.SurfaceType):
    R = pg.surfarray.pixels_red(img).T
    G = pg.surfarray.pixels_green(img).T
    B = pg.surfarray.pixels_blue(img).T
    return np.average(np.stack([R,G,B]), axis=0)


#-------main------------
image = pg.image.load("download.jpg")
image = pg.transform.scale(image, (120, 120))
W,H = 120,240
w,h = char_width,char_height
columns =int(W/char_width) 
rows = int(H/char_height)

image = get_pixel_arrays(image)
print(image.shape)

max_val = np.max(image)
min_val = np.min(image)
#print(max_val,min_val)
#print(len(aimg))
j=0
for j in range(120):
    k=0
    pic=""
    for k in range(240):
        ch = get_char_for_value(image[j,k],min_val,max_val,characters,grayscale)
        pic = pic+ch
    print(pic)	
   