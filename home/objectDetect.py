import cv2
import numpy as np
from _collections import defaultdict

# Load Yolo
labels = []
myDict = defaultdict(list)
functionDict = defaultdict(list)

def work(myImage):


    img = myImage
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    classes = []
    with open("coco.names","r") as f:
        classes = [line.strip() for line in f.readlines()]

    layer_names = net.getLayerNames()
    outputLayers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes)+2, 3))

    # with output layer can get the final detection of the object

    # Loading image

    img = cv2.resize(img,None, fx=.3, fy=.3)
    height, width, channels = img.shape


    # detetcting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    # for b in blob:
    #     for n, img_blob in enumerate(b):
    #         cv2.imshow(str(n), img_blob)

    net.setInput(blob)
    outs = net.forward(outputLayers)


    # Showing information on the screen

    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:          #object detetcted
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                #cv2.circle(img, (center_x, center_y), 5, (0, 255, 0), 2)

                # Rectangle co ordinates

                x = int(center_x-w/2)
                y = int(center_y - h/2)

                #cv2.rectangle(img, (x, y), ( x+w, y+h), (0, 255, 0), 1)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)




    #print(len(boxes))
    #number_objects_detected = len(boxes)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    #print(indexes)

    font = cv2.FONT_HERSHEY_PLAIN
    j = 1
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            print(i)
            label = str(classes[class_ids[i]])
            color = colors[i]
            #print(label),print(boxes[i])
            image2 = cv2.resize(myImage,None, fx=.3, fy=.3)
            cv2.rectangle(image2, (x, y), (x + w, y + h), color, 1)
            cv2.putText(image2, label, (x, y + 20), font, 1, color, 2)
            cv2.imwrite("objectImage/" + label +str(i)+ ".jpg", image2)
            list = []
            list.append(x)
            list.append(y)
            list.append(w)
            list.append(h)

            myDict[label].append(list)



            cv2.rectangle(img, (x, y), (x + w, y +h), color, 1)
            cv2.putText(img, label, (x, y+20), font, 1, color, 2)
            #cv2.imwrite("media/" + label + ".jpg", img)


    #return img


