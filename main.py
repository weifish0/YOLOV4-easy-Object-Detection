import cv2
from cv2 import VideoCapture
from cv2 import dnn_DetectionModel
import numpy as np
import matplotlib as plt

# opencv DNN
net = cv2.dnn.readNet('./dnn_model/yolov4-tiny.weights', './dnn_model/yolov4-tiny.cfg')
model = cv2.dnn_DetectionModel(net)
# 調整 DNN 與 opencv 的基本參數
model.setInputParams(size = (416,416), scale = 1/255)

# 模型偵測 txt
classes = []
with open("./dnn_model/classes.txt", 'r') as file_object:
    for class_name in file_object.readlines():
        classname = class_name.strip()
        classes.append(class_name)
        
# 相機刷新
cap = cv2.VideoCapture("./utils/Alisa Stewart Honor Walk.mp4")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


while cap.isOpened():
    # 解讀相機拍到的圖片
    ret, frame = cap.read()
    if not ret:
        print("找不到影像輸入")
        break
    
    # 物件偵測 (引用訓練好的模型) 
    (class_ids, scores, bboxes) = model.detect(frame)
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y, w, h)= bbox
        class_name = classes[class_id]
        # print(bbox)
        # 繪製框框與偵測到的物件資訊
        cv2.putText(frame, class_name, (x, y-7), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (139,61,72),2)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,102,178), 3)
    # print('class_ids', class_ids)
    # print('score', scores)
    # print('bboxes', bboxes)
    # 展示圖片與停頓(構成影片)
    cv2.imshow('test', frame)
    if cv2.waitKey(1) == ord('q'):
        break
