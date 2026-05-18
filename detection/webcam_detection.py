import cv2
import torch
from ultralytics import YOLO

model = YOLO(r"runs\train-2\weights\best.pt")

device = 0 if torch.cuda.is_available() else "cpu"

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame, conf=0.5, device=device)

    annotated = results[0].plot()

    cv2.imshow("YOLO Fire Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()