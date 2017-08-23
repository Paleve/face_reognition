# -*- coding:utf-8 -*-
from multiprocessing import Process,Queue
import time
import face_recognition
import os
import cv2
import dlib

is_show_img=1
def entry(q_entry):
    #cam_entry=cv2.VideoCapture('/home/x/视频/Webcam/2017-08-14-152626.webm')
    cam_entry=cv2.VideoCapture(2)
    entry_detector = dlib.get_frontal_face_detector()
    ret_val, img_entry = cam_entry.read()
    print 'entry ret_val: ',ret_val
    count=0
    while ret_val:
        is_person = 0
        dets = entry_detector(img_entry, )
        for i, d in enumerate(dets):
            is_person+=1
            left, top, right, bottom = d.left(), d.top(), d.right(), d.bottom()
            cv2.rectangle(img_entry, (left, top), (right, bottom), (0, 0, 255))

        if is_person==1:

            #cv2.imwrite('pic/'+str(count)+'.jpg',img_entry)

            #img_entry = cv2.cvtColor(img_entry, cv2.COLOR_BGR2RGB)
            entry_time_stamp=time.time()
            q_entry.put([count, img_entry,dets,entry_time_stamp])
            count+=1
        if is_show_img==1:
            cv2.imshow('entry', img_entry)
            cv2.waitKey(1)

        ret_val, img_entry = cam_entry.read()

    cam_entry.release()
def exit(q_exit):
    #cam_exit=cv2.VideoCapture('/home/x/视频/Webcam/2017-08-14-152626.webm')
    cam_exit = cv2.VideoCapture(0)
    exit_detector = dlib.get_frontal_face_detector()
    ret_val,img_exit=cam_exit.read()
    print 'exit ret_val: ',ret_val
    count=0
    while ret_val:
        is_person=0
        dets = exit_detector(img_exit, )
        for i, d in enumerate(dets):
            is_person+=1
            left, top, right, bottom = d.left(), d.top(), d.right(), d.bottom()
            cv2.rectangle(img_exit, (left, top), (right, bottom), (0, 0, 255))


        if is_person==1:
            #img_exit = cv2.cvtColor(img_exit, cv2.COLOR_BGR2RGB)
            q_exit.put([count,img_exit,dets])
            count+=1
        if is_show_img==1:
            cv2.imshow('exit', img_exit)
            cv2.waitKey(1)
        ret_val, img_exit = cam_exit.read()

    cam_exit.release()
def recognize(q_entry_code,q_exit_code):
    persondict={}
    while 1:

        if not q_entry_code.empty():
            print 'persondict', len(persondict)
            print 'q_entry_code.qsize:',q_entry_code.qsize()

            q_entry_data=q_entry_code.get()
            personID = q_entry_data[0]
            img_entry_encoding = q_entry_data[1]

            if personID in persondict.keys():
                persondict[personID].append(img_entry_encoding)
            else:
                persondict[personID]=[]
                persondict[personID].append(img_entry_encoding)

        if not q_exit_code.empty():
            print 'persondict', len(persondict)
            print 'q_exit_code.qsize:',q_exit_code.qsize()
            q_exit_data=q_exit_code.get()
            exit_personID=q_exit_data[0]
            img_exit_encoding=q_exit_data[1]

            for personID in persondict.keys():
                results = face_recognition.compare_faces(persondict[personID], img_exit_encoding, 0.4)
                if sum(results)>=1:
                    print results
                    print "\nthis predict person is ",personID,"  exit person is ",exit_personID
                    print "send message......"
                    print "delete this people"
                    persondict.pop(personID)
                    break



if __name__ == '__main__':
    #facepath = '../../documents/Images_min/'
    #imglist = os.listdir(facepath)


    q_entry = Queue()
    q_exit = Queue()
    q_entry_code = Queue()
    q_exit_code = Queue()
    p1 = Process(target=entry, args=(q_entry,))
    p2 = Process(target=exit, args=(q_exit,))
    p3 = Process(target=recognize, args=(q_entry_code, q_exit_code,))
    p1.start()
    p2.start()
    p3.start()
    while 1:
        if not q_entry.empty():
            q1data=q_entry.get()
            personID=q1data[0]
            img_entry=q1data[1]
            entry_face_loc = q1data[2]
            entry_time_stamp=q1data[3]
            img_entry_encoding = face_recognition.face_encodings(img_entry,entry_face_loc)
            if len(img_entry_encoding) == 1:
                img_entry_encoding=img_entry_encoding[0]
                q_entry_code.put([personID,img_entry_encoding,entry_time_stamp])


        if not q_exit.empty():
            q2data=q_exit.get()
            real_personID = q2data[0]
            img_exit=q2data[1]
            exit_face_loc = q2data[2]
            img_exit_encoding = face_recognition.face_encodings(img_exit,exit_face_loc)
            if len(img_exit_encoding) == 1:
                img_exit_encoding = img_exit_encoding[0]

                q_exit_code.put([real_personID, img_exit_encoding])
