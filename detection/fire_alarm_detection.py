from collections import deque
import cv2
import torch
from ultralytics import YOLO
import pygame

model = YOLO(r"runs\train-2\weights\best.pt")

device = 0 if torch.cuda.is_available() else "cpu"

pygame.mixer.init()

sound_path = r"sounds\fire_alarm.mp3"

cap = cv2.VideoCapture(0)

fire_active = False

history = deque(maxlen=5)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame, conf=0.6, device=device)

    annotated = results[0].plot()

    boxes = results[0].boxes

    fire_detected = len(boxes) > 0

    history.append(fire_detected)

    confirmed_fire = history.count(True) >= 3

    if confirmed_fire and not fire_active:

        fire_active = True

        pygame.mixer.music.load(sound_path)

        pygame.mixer.music.play(-1)

    elif not confirmed_fire and fire_active:

        fire_active = False

        pygame.mixer.music.stop()

    cv2.imshow("YOLO Fire Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()