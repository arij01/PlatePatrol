from ultralytics import YOLO
import cv2


# load models.\venv\Scripts\activate
coco_model = YOLO('yolov8n.pt')
license_plate_detector = YOLO('./model')

# load video
cap = cv2.VideoCapture('C:/Users/21626/Videos/sample.mp4')

# read frames

# detect vehicles
      
 # track vehicles

# detect license plates

# assign license plate to car

# crop license plate

# process license plate

# read license plate number

# write results
