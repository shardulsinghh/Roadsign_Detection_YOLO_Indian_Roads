import os
from PIL import Image


def form_cmd(image_name):
    return './darknet detector test cfg/obj.data yolo-obj.cfg backup/yolo-obj_last.weights data/obj/' + image_name

image_name = input('Enter Test Image Name:')
cmd = form_cmd(image_name)

os.system(cmd)
print('Displaying Results:')
prediction = Image.open('predictions.jpg')
prediction.show()



