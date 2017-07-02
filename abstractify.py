import numpy as np
import sys
import cv2

def initialize(image):
	img = cv2.imread(image)
	grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(grayed, (51,51), 0)
	return blurred


def posterize(image, level):
	indices = np.arange(0,256)
	divider = np.linspace(0,255,level+1)[1]
	quantiz = np.int0(np.linspace(0,255,level))
	color_levels = np.clip(np.int0(indices/divider),0,level-1)
	palette = quantiz[color_levels]
	img2 = palette[image]
	img2 = cv2.convertScaleAbs(img2)
	return img2

if __name__  == '__main__' :
	initial = initialize(sys.argv[1])
	poster = posterize(initial,6)
	colorized = cv2.applyColorMap(poster, cv2.COLORMAP_RAINBOW)
	cv2.imwrite("current_output.png", colorized)

"""
0	COLORMAP_AUTUMN
1	COLORMAP_BONE
2	COLORMAP_JET
3	COLORMAP_WINTER
4	COLORMAP_RAINBOW
5	COLORMAP_OCEAN
6	COLORMAP_SUMMER
7	COLORMAP_SPRING
8	COLORMAP_COOL
9	COLORMAP_HSV
10	COLORMAP_PINK
11	COLORMAP_HOT
"""