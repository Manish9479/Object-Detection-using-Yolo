from ultralytics import YOLO
import cv2

model = YOLO('../Yolo-Weights/yolov8n.pt')
results = model("Running Yolo\IMAGES\helmet_jacket_07381.jpg", show=True)
cv2.waitKey(0)

