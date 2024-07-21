from ultralytics import YOLO
import cv2


# load models.\venv\Scripts\activate
coco_model = YOLO('yolov8n.pt')
license_plate_detector = YOLO('./model')

# load video
cap = cv2.VideoCapture('C:/Users/21626/Videos/sample.mp4')

# read frames
frame_nmr = -1
ret = True
while ret:
    frame_nmr += 1
    ret, frame = cap.read()
    if ret and frame_nmr < 10:
        
        # detect vehicles
        detections = coco_model(frame)[0]
        print(detections)

      
        # track vehicles

        # detect license plates

        # assign license plate to car

        # crop license plate

        # process license plate

        # read license plate number

        # write results
