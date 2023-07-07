import cv2
from ultralytics import YOLO
import math
# import cvzone

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

def calculate_vehicles(num):
    model=YOLO("./yolo-weights/yolov8x.pt")

    classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
                "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
                "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
                "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
                "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
                "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
                "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
                "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
                "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
                "teddy bear", "hair drier", "toothbrush"]

    car=0
    bicycle=0
    motorbike=0
    bus=0
    truck=0

    img=cv2.imread(f"./Images/{num}.jpg")
    resized_img=rescaleFrame(img)

    result=model(resized_img,show=True)
    for r in result:
        boxes=r.boxes
        for box in boxes:
            cls=int(box.cls[0])
            conf=math.ceil(box.conf[0]*100)/100
            currentclass=classNames[cls]
            if(conf>0.5):
                if currentclass=='car':
                    car+=1
                elif currentclass=='bicycle':
                    bicycle+=1
                elif currentclass=='motorbike':
                    motorbike+=1
                elif currentclass=='bus':
                    bus+=1
                elif currentclass=='truck':
                    truck+=1

    sum=car+motorbike+bicycle+bus+truck
    print(f'Car: {car}\nMotorBike: {motorbike}\nBicycle: {bicycle}\nBus: {bus}\nTruck: {truck}\nTotal Vehicles: {sum}')
    cv2.waitKey(0)
    return sum

# calculate_vehicles(5)