# -*- coding: utf-8 -*-
import cv2
import numpy as np
#拆分及合并图像通道

img=cv2.imread('../data/messi5.jpg')

#
b,g,r=cv2.split(img)#比较耗时的操作，请使用numpy 索引
img=cv2.merge(b,g,r)

#
b=img[:,:,0]

#使所有像素的红色通道值都为 0,你不必先拆分再赋值。
# 你可以 直接使用 Numpy 索引,这会更快。
img[:,:,2]=0




