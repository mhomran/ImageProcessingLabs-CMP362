from commonfunctions import *
import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np

from skimage.exposure import rescale_intensity

# Show the figures / plots inside the notebook
# %matplotlib inline
from skimage.color import rgb2gray
from skimage import exposure


def Negative(Original, Converted, thr):
    for i in range(0, Converted.shape[0]-1):
        for j in range(0, Converted.shape[1]-1):
            pixelColorVals = Converted[i, j]
            redPixel = 255 - pixelColorVals[0]    # Negate red pixel
            greenPixel = 255 - pixelColorVals[1]  # Negate green pixel
            bluePixel = 255 - pixelColorVals[2]   # Negate blue pixel
            Converted[i, j] = [redPixel, greenPixel,
                               bluePixel, pixelColorVals[3]]
    show_images([Original, Converted], ["Original Image", "Negative Image"])


def Contrast_enhancement(Original, ContrastImg):

    for i in range(0, ContrastImg.shape[0]):
        for j in range(0, ContrastImg.shape[1]):

            pixelColorVals = ContrastImg[i, j]

            if(0 <= pixelColorVals <= 100):
                pixelColorVals = np.int32(1.5*pixelColorVals+50)

            ContrastImg[i, j] = pixelColorVals
    show_images([Original, ContrastImg], ["Original Image", "ContrastImg"])


def Gamma_Correction(Original, gamma):
    gamma_corrected = exposure.adjust_gamma(Original, gamma)
    show_images([Original, gamma_corrected], [
                "Original Image", "gamma_corrected "])


'''
1
Negative Transformation
'''

# Original = io.imread('imgs/Picture1.png')
# Converted = np.copy(Original)
# Negative(Original, Converted, 0)


'''
2
Contrast Enhancement
'''

Original = rgb2gray(io.imread('imgs/Picture2.png'))
img = rescale_intensity(Original, in_range=(0, 1.0), out_range=(0, 255))

img = img.astype(np.int32)

ContrastImg = np.copy(img)
Contrast_enhancement(img, ContrastImg)

'''
3
Gamma Correction
'''
Original = io.imread('imgs/Picture2.png')
# Gamma
# Gamma_Correction(Original, 3)
# Gamma_Correction(Original, .5)


'''
4 Histogram Eq.
Note: Histogram function of skimage returns only present intensity values not all 255
You can use showHist function from commonfunctions file
'''


def getImageWithHist(name, ext, nbins=256):
    pass
