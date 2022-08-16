import cv2 as cv
# cv.cvtColor()函数灰度处理
# 原始读入为BGR格式
img = cv.imread("test_data/dog.png")
# 交换通道顺序 BGR->GRB
# summarize: COLOR_BGR2GRAY：原格式->灰度处理
#            COLOR_RGB2GRAY：原格式->RGB变换->灰度处理 especially:原格式为RGB<=>BGR->灰度处理
img_RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# BGR->GRAY
img_gray_0 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# RGB->GRAY
img_gray_1 = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
# RGB->GRAY BGR(RGB)=RGB
img_gray_2 = cv.cvtColor(img_RGB, cv.COLOR_BGR2GRAY)
# BGR->GRAY RGB(RGB)=BGR
img_gray_3 = cv.cvtColor(img_RGB, cv.COLOR_RGB2GRAY)

cv.imshow("img_GRAY_0",img_gray_0)
cv.imshow("img_GRAY_1",img_gray_1)
cv.imshow("img_GRAY_2",img_gray_2)
cv.imshow("img_GRAY_3",img_gray_3)
cv.waitKey(0)
cv.destroyAllWindows()