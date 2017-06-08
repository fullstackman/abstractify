import numpy as np
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/')
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

initial = initialize(sys.argv[1])
poster = posterize(initial,6)
cv2.imwrite("topo_image.png", poster)
