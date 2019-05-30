import os
from PIL import Image
import cv2
import os
import shutil

def form_cmd(image_name):
    return './darknet detector test cfg/obj.data yolo-obj.cfg backup/yolo-obj_last.weights data/obj/' + image_name

cam = cv2.VideoCapture(0)

cv2.namedWindow("YOLO")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("YOLO", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "saved_frame.jpg"
        # cv2.imwrite(img_name, frame)
        resized_image = cv2.resize(frame, (400, 400)) 
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        cmd = form_cmd(img_name)
        try:
            os.rename("/Users/shardulvikramsingh/Alpha/Object_Detection/darknet/saved_frame.jpg", "/Users/shardulvikramsingh/Alpha/Object_Detection/darknet/data/obj/saved_frame.jpg")
        except FileNotFoundError:
            print('File Not Found')
            print("Trying Again in 2 sec")
            os.rename("/Users/shardulvikramsingh/Alpha/Object_Detection/darknet/saved_frame.jpg", "/Users/shardulvikramsingh/Alpha/Object_Detection/darknet/data/obj/saved_frame.jpg")
        
        os.system(cmd)
        print('Displaying Results:')
        prediction = Image.open('predictions.jpg')
        prediction.show()


cam.release()

cv2.destroyAllWindows()


# image_name = input('Enter Test Image Name:')
# cmd = form_cmd(image_name)

# os.system(cmd)
# print('Displaying Results:')
# prediction = Image.open('predictions.jpg')
# prediction.show()




