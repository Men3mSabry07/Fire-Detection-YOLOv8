# 🔥 Fire Detection & Alert System using YOLOv8

A real-time Fire Detection and Alert System built using **YOLOv8** and **Computer Vision** techniques.  
The system detects fire from live camera streams and triggers an alarm system for early warning and safety monitoring.

---

## 📌 Overview

This project focuses on building a deep learning-based fire detection system capable of:

- Detecting fire in real-time using webcam input
- Running efficient object detection using YOLOv8
- Triggering an alarm when fire is confirmed
- Supporting both lightweight and advanced training configurations
- Providing real-time visual detection with bounding boxes

The project was developed as part of an academic deep learning and computer vision project.

# 👨‍💻 Team Members

<div align="center">

Abdelmonem Sabry • Ali Omar Salama • Abdullah Mohamed Salah • Madonna Ashraf Fakhry

</div>

---

# 👨‍🏫 Supervision

- **Instructor:** Dr. Asmaa Abbas Hassan
- **Mentor:** Eng. Ali Osama

---

# 🗂️ Project Structure

```bash
Fire-Detection-System/
│
├── detection/
│   ├── fire_alarm_detection.py
│   └── webcam_detection.py
│
├── sounds/
│   └── fire_alarm.mp3
│
├── train/
│   ├── train_yolov8n.py
│   ├── train_yolov8m.py
│   └── resume_training.py
│
├── weights/
│   ├── best.pt
│   └── last.pt
│
└── README.md
```

# 📊 Dataset

The project uses the **Continuous Fire Dataset** for training and evaluation.

### Dataset Statistics

| Split | Images |
|------|------|
| Train | 1004 |
| Validation | 754 |
| Test | 751 |
| Total | 2509 |

### Dataset Link

https://universe.roboflow.com/-jwzpw/continuous_fire/dataset/6

---

# ⚙️ Training Configurations

Two different YOLOv8 configurations were tested during experimentation.

## 🔹 Experiment 1 — YOLOv8n

| Parameter | Value |
|---|---|
| Model | YOLOv8n |
| Epochs | 50 |
| Image Size | 416×416 |

---

## 🔹 Experiment 2 — YOLOv8m

| Parameter | Value |
|---|---|
| Model | YOLOv8m |
| Epochs | 100 |
| Image Size | 640×640 |
| Batch Size | 10 |
| AMP | Enabled |
| Cosine LR | Enabled |

---

# 📈 Results

## YOLOv8n Results

| Metric | Value |
|---|---|
| Precision | 0.872 |
| Recall | 0.680 |
| mAP@0.5 | 0.823 |
| mAP@0.5:0.95 | 0.599 |

---

## YOLOv8m Results

| Metric | Value |
|---|---|
| Precision | 0.837 |
| Recall | 0.743 |
| mAP@0.5 | 0.846 |
| mAP@0.5:0.95 | 0.568 |

---

# 🎥 Real-Time Detection

The system supports real-time webcam fire detection with:

- Live bounding box visualization
- Confidence-based predictions
- Alarm activation on confirmed fire detection
- False positive reduction using frame history confirmation

---

# 🚨 Alarm System Logic

The alarm system was implemented using `pygame` and works as follows:

- The model analyzes consecutive frames from the webcam
- Fire detection history is stored temporarily
- Alarm is triggered only after multiple positive detections
- Alarm stops automatically when fire disappears

This approach helps reduce false alarms and improves system stability.

---

#  Challenges Faced

During development, several challenges were encountered:

- Dataset labeling inconsistency
- Different image qualities across datasets
- Hardware limitations during training
- Generalization issues after dataset merging
- False positives in difficult lighting conditions

---

#  Future Improvements

- Mobile notification integration
- IoT alarm integration
- Cloud deployment support
- Smoke detection enhancement
- Edge-device optimization
- Larger and more diverse datasets

---

#  Training Results

Google Colab Results Notebook:

https://colab.research.google.com/drive/1papIS4YPooGFm3GVOy4V_oLNEavvKxzS?usp=sharing

#  Conclusion

This project demonstrates how deep learning and computer vision can be applied to build a practical real-time fire detection system.

The experiments showed that YOLOv8 can achieve strong detection performance while maintaining real-time inference speed, making the system suitable as a foundation for early fire warning applications.

---
