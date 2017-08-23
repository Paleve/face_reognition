# This script is to extract feature from img
# Storage format is {name1:[vec1,vec2,...],name2:[vec1,vec2,...],name3:[vec1,vec2,...]...}
# 2017/8/11 by zts

import cv2
import face_recognition
import numpy as np
import os
import pickle

img_path = './data'
data = {}

path_flag = os.path.isdir(img_path)

if (path_flag):
    for file_package_name in os.listdir(img_path):
        name = file_package_name

        feature_list = []

        for filename in os.listdir(img_path+'/'+file_package_name):

            # feature_list is to store img feature for one person
            file_dir = img_path+'/'+file_package_name+'/'+filename

            img = face_recognition.load_image_file(file_dir)

            try:
                my_face_encoding = face_recognition.face_encodings(img)[0]
                # put all vecs into one list for every person
                feature_list.append(my_face_encoding)
            except:
                pass

        # {name:[vec1,vec2,...]}
        name_feature_dic = {name: feature_list}
        # print name_feature_dic
        data = dict(data.items() + name_feature_dic.items())
# print data

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data, output)

output.close()