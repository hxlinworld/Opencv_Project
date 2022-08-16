import cv2 as cv
#  导入 matplotlib
import matplotlib.pyplot as plt
img = cv.imread("test_data/dog.png")

# 更换通道顺序，将图像BGR->RGB
# 使用matplotlib变换
# img_RGB = img[:,:,(2, 1, 0)]
# cvtColor变换
img_RGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)

# 定义图片显示大小
top_size,button_size,left_size,right_size = (50,50,50,50)

# 复制法，复制最边缘像素
replicate = cv.copyMakeBorder(img_RGB,top_size,button_size,left_size,right_size,borderType=cv.BORDER_REPLICATE)

# 反射法，对感兴趣的图像中的像素在两边进行复制
reflect = cv.copyMakeBorder(img_RGB,top_size,button_size,left_size,right_size,borderType=cv.BORDER_REFLECT)

# 反射法，以最边缘像素为轴、对称
reflect101 = cv.copyMakeBorder(img_RGB,top_size,button_size,left_size,right_size,borderType=cv.BORDER_REFLECT_101)

# 外包装法
wrap = cv.copyMakeBorder(img_RGB,top_size,button_size,left_size,right_size,borderType=cv.BORDER_WRAP)

# 常量法，常数值填充
constant = cv.copyMakeBorder(img_RGB,top_size,button_size,left_size,right_size,borderType=cv.BORDER_CONSTANT)

# 设置图像位置
plt.subplot(231)
# 设置图像显示
plt.imshow(img_RGB,'gray')
# 设置标题
plt.title('ORIGINAL')

plt.subplot(232)
plt.imshow(replicate,'gray')
plt.title("REPLICATE")

plt.subplot(233)
plt.imshow(reflect,'gray')
plt.title("REFLECT")

plt.subplot(234)
plt.imshow(reflect101,'gray')
plt.title("REPLICATE101")

plt.subplot(235)
plt.imshow(wrap,'gray')
plt.title("WRAP")

plt.subplot(236)
plt.imshow(constant,'gray')
plt.title("CONSTANT")





plt.show()
