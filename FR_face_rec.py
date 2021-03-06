from __future__ import division
import face_recognition
import cv2
import pickle

pkl_file = open('data.pkl', 'rb')

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

#open webcam
video_capture = cv2.VideoCapture(0)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True



while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(frame)
        print len(face_locations)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            for name in data:
                feature_list = data[name]
                # print feature_list
                match = face_recognition.compare_faces(feature_list, face_encoding,tolerance=0.4)

                if judge(match) == True:
                    print name
                    # face_names.append(name)
                # if judge(match) == False:
                    # print 'Unknow'

        # # Display the results
        # for (top, right, bottom, left), name in zip(face_locations, face_names):
        #     # Draw a box around the face
        #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #
        #     # Draw a label with a name below the face
        #     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255))
        #     font = cv2.FONT_HERSHEY_DUPLEX
        #     cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()