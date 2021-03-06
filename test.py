import cv2
im_gray = cv2.imread('image_depth.jpg', cv2.IMREAD_GRAYSCALE)
#Convert grayscale image to binary

(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#which determines the threshold automatically from the image using Otsu's method, or if you already know the threshold you can use:

thresh = 127
im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
#Save to disk

cv2.imwrite('bw_image.png', im_bw)
# cv2.imshow('bw_image.png')

