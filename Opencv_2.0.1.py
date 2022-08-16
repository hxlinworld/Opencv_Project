import cv2 as cv

img = cv.imread("test_data/dog.png")
cv.imshow("img",img)
# img = img[:,:,(2, 1, 0)] #add


# 定义图片显示大小
top_size,button_size,left_size,right_size = (50,50,50,50)
# 复制法，复制最边缘像素
replicate = cv.copyMakeBorder(img,top_size,button_size,left_size,right_size,borderType=cv.BORDER_REPLICATE)
cv.imshow("replicate",replicate)
# 反射法，对感兴趣的图像中的像素在两边进行复制
reflect = cv.copyMakeBorder(img,top_size,button_size,left_size,right_size,borderType=cv.BORDER_REFLECT)
cv.imshow("reflect",reflect)
# 反射法，以最边缘像素为轴、对称
reflect101 = cv.copyMakeBorder(img,top_size,button_size,left_size,right_size,borderType=cv.BORDER_REFLECT_101)
cv.imshow("reflect101",reflect101)
# 外包装法
wrap = cv.copyMakeBorder(img,top_size,button_size,left_size,right_size,borderType=cv.BORDER_WRAP)
cv.imshow("wrap",wrap)
# 常量法，常数值填充
constant = cv.copyMakeBorder(img,top_size,button_size,left_size,right_size,borderType=cv.BORDER_CONSTANT)
cv.imshow("constant",constant)
cv.waitKey(0)
cv.destroyAllWindows()