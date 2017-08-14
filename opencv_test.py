import cv2

# cap = cv2.VideoCapture(0)
# while(1):
#     # get a frame
#     ret, frame = cap.read()
#     # show a frame
#     cv2.imshow("capture", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         cv2.imwrite("/opt/code/image/fangjian2.jpeg", frame)
#         break
# cap.release()
# cv2.destroyAllWindows()

img = cv2.imread('./data/ym/ym_1.jpg')
print img
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()