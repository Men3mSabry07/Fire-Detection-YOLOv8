from ultralytics import YOLO
import torch

def main():

    device = 0 if torch.cuda.is_available() else "cpu"

    model = YOLO("yolov8n.pt")

    model.train(
        data=r"Data\data.yaml",
        epochs=50,
        imgsz=416,
        device=device,
        workers=0
    )

if __name__ == "__main__":
    main()