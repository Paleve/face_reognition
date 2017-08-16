# -*- coding: UTF-8 -*-
# 导入相关的库
from sys import argv
from base64 import b64encode
import base64
import json
from json import dumps
import cv2
ENCODING = 'utf-8'    # 指定编码形式

JSON_NAME = 'argv'    # 获得文件名参数



#----------------------------------------------
# # 读取二进制图片，获得原始字节码，注意 'rb'
# IMAGE_NAME = './data/an/ym_2.jpg'
# with open(IMAGE_NAME, 'rb') as jpg_file:
#     byte_content = jpg_file.read()
# # 把原始字节码编码成 base64 字节码
# base64_bytes = b64encode(byte_content)
# # 将 base64 字节码解码成 utf-8 格式的字符串
# base64_string = base64_bytes.decode(ENCODING)
# # 用字典的形式保存数据
# raw_data = {}
# raw_data["name"] = IMAGE_NAME
# raw_data["image_base64_string"] = base64_string
# # 将字典变成 json 格式，缩进为 2 个空格
# json_data = dumps(raw_data, indent=2)
# # 将 json 格式的数据保存到文件中
# with open(JSON_NAME, 'w') as json_file:
#     json_file.write(json_data)

#------------------------------------------------

# 读取 json 文件，并直接存入字典
IMAGE_NAME = '1.jpg'
with open(JSON_NAME, "r") as json_file:
    raw_data = json.load(json_file)
# 从字典中取得图片的 base64 字符串，形如“YABgAAD/2wBDAAYEBQYFBAY...."，
image_base64_string = raw_data["image_base64_string"]
# 将 base64 字符串解码成图片字节码
image_data = base64.b64decode(image_base64_string)
# print image_data
# 将字节码以二进制形式存入图片文件中，注意 'wb'
with open(IMAGE_NAME, 'wb') as jpg_file:
    jpg_file.write(image_data)
#
# img = cv2.imread('1.jpg')
# cv2.imshow('img',img)
# cv2.waitKey(0)