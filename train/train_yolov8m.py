from ultralytics import YOLO
import torch

def main():

    device = 0 if torch.cuda.is_available() else "cpu"

    model = YOLO("yolov8m.pt")

    model.train(
        data=r"Data\data.yaml",
        epochs=100,
        imgsz=640,
        batch=10,
        device=device,
        workers=2,
        cache=True,
        amp=True,
        cos_lr=True
    )

if __name__ == "__main__":
    main()