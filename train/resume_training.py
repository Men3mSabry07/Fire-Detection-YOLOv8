from ultralytics import YOLO
import torch

def main():

    device = 0 if torch.cuda.is_available() else "cpu"

    model = YOLO(r"runs\detect\train-5\weights\last.pt")

    model.train(
        data= r"Data\data.yaml",
        epochs=100,
        imgsz=640,
        batch=8,
        device=device,
        workers=2,
        cache=False,
        amp=True,
        patience=20,
        cos_lr=True,
        resume=True
    )

if __name__ == "__main__":
    main()