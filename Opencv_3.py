import cv2 as cv

img = cv.imread("test_data/dog.png")
img_BG = cv.imread("test_data/grass.png")
# 显示图像的尺寸数值
print(img.shape)
print(img_BG.shape)
# 设置两张图像尺寸数值相同
img = cv.resize(img,(610,400))
print(img.shape)
# 融合两张图像，设置好权重值
res = cv.addWeighted(img,0.6,img_BG,0.4,0)
# 保存融合后的图像
cv.imwrite("test_data/res.png",res)

cv.imshow("res_result",res)
cv.waitKey(0)
cv.destroyAllWindows()



