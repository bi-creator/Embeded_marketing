# from skimage import io
from PIL import Image
import requests
from io import BytesIO
import cv2
import numpy


def imagematching(testimage, imageurl):
    # test image

    # image = cv2.imread(testimage)
    gray_image = cv2.cvtColor(testimage, cv2.COLOR_BGR2GRAY)
    histogram = cv2.calcHist([gray_image], [0],
                             None, [256], [0, 256])

    # data1 image
    response = requests.get(imageurl)
    img = Image.open(BytesIO(response.content)).convert('RGB')
    open_cv_image = numpy.array(img)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    # image_comp = io.imread(
    #     'https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcTx7kXXGRxqdthhznW7pdOAQTB-0iyHen-mxJ-oTzyhJMHI3tIZHHO6_IpDtjREqn8iMt_8QQgUbbv-q8y4heWBfBJT4iawMe8wLXJVTXJSKrQbyVDz8jkSuA&usqp=CAE')
    # image = cv2.imread(image_comp)
    gray_image1 = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    histogram1 = cv2.calcHist([gray_image1], [0],
                              None, [256], [0, 256])

    c1 = 0

    # Euclidean Distance between data1 and test
    i = 0
    while i < len(histogram) and i < len(histogram1):
        c1 += (histogram[i]-histogram1[i])**2
        i += 1
    c1 = c1**(1 / 2)

    return(float(c1[0]))
