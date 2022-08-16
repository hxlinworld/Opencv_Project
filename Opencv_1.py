
# 导入 OpenCV 库
import cv2 as cv
import matplotlib.pyplot as plt
# 显示原图
# 读取图像
img = cv.imread("test_data/dog.png")
# 打印图像类型 ->返回numpy型
print(type(img))

# 显示图像
cv.imshow("dog",img)
# 图像驻留，按任意键终止
cv.waitKey(0)
cv.destroyAllWindows()

# 显示灰度图像
img_gray = cv.imread("test_data/dog.png",cv.IMREAD_GRAYSCALE)
cv.imshow("dog_gray",img_gray)
cv.waitKey(0)
cv.destroyAllWindows()

# 截取部分图像
img_cut = img[150:400,150:400]
cv.imshow("dog_cut",img_cut)
cv.waitKey(0)
cv.destroyAllWindows()

# 颜色通道提取
b,g,r = cv.split(img)
cv.imshow('BLUE',b)
cv.imshow('GREEN',g)
cv.imshow('RED',r)
# 合并三个通道
img_merge = cv.merge([b,g,r])
cv.imshow('img_merge',img_merge)



# 保留R通道图像->红狗
RED_img = img.copy()
# BGR->去除B通道
RED_img[:,:,0] = 0
# 去除G通道
RED_img[:,:,1] = 0
cv.imshow('RED_dog',RED_img)


# 保留G通道图像->绿狗
GREEN_img = img.copy()
# BGR->去除B通道
GREEN_img[:,:,0] = 0
# 去除R通道
GREEN_img[:,:,2] = 0
# cv.imshow('GREEN_dog',GREEN_img)

# 保留B通道图像->蓝狗
BLUE_img = img.copy()
# BGR->去除G通道
BLUE_img[:,:,1] = 0
# 去除R通道
BLUE_img[:,:,2] = 0
# cv.imshow('BLUE_dog',BLUE_img)

cv.waitKey(0)
cv.destroyAllWindows()
