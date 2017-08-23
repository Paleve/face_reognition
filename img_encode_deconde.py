# -*- coding: UTF-8 -*-
# 导入相关的库
from sys import argv
from base64 import b64encode
import base64
import json
from json import dumps
# import cv2
# import face_recognition
ENCODING = 'utf-8'    # 指定编码形式

JSON_NAME = 'argv'    # 获得文件名参数



#----------------------------------------------
# # 读取二进制图片，获得原始字节码，注意 'rb'
IMAGE_NAME = './data/tsy/tsy_68.jpg'
IMAGE_NAME1 = '1.jpg'
with open(IMAGE_NAME, 'rb') as jpg_file:
    byte_content = jpg_file.read()
# 把原始字节码编码成 base64 字节码
base64_bytes = b64encode(byte_content)
print  (base64_bytes)

# ##使用本地编码
# # base64_bytes =
# image_data = base64.b64decode(base64_bytes)
# print ('image_data',image_data)
#
#
# with open(IMAGE_NAME1, 'wb') as jpg_file:
#     jpg_file.write(image_data)
# #
# img = cv2.imread(IMAGE_NAME1)
#
# face_locations = face_recognition.face_locations(img)
# print (face_locations)
# print (len(face_locations))
# cv2.imshow('img',img)
# cv2.waitKey(0)



