from __future__ import division

from flask import Flask, request
import face_recognition
from base64 import b64encode
import cv2
import base64
import pickle
app = Flask(__name__)

PORT = 6070
HOST = '0.0.0.0'
IMAGE_NAME = 'save.jpg'
pkl_file = open('data.pkl', 'rb')
ENCODING = 'utf-8'

data = pickle.load(pkl_file)
# print data

pkl_file.close()

def judge(list):
    #is to judge whether the person is recongnized
    length = len(list)
    True_num = 0
    for flag in list:
        if flag:
            True_num += 1
        else:
            pass
    if True_num / length >= 0.5:
        return True
    else:
        return False

@app.route('/')
def hello():
    base64_bytes = request.args.get('img')

    # return 'conneted receive %s' % base64_bytes

    image_data = base64.b64decode(base64_bytes.replace(' ','+'))

    with open(IMAGE_NAME, 'wb') as jpg_file:
        jpg_file.write(image_data)

    frame = cv2.imread(IMAGE_NAME)

    face_locations = face_recognition.face_locations(frame)

    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        for name in data:
            feature_list = data[name]
            # print feature_list
            match = face_recognition.compare_faces(feature_list, face_encoding, tolerance=0.4)

            if judge(match) == True:
                return name
            else:
                return 'Unknow'

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)


