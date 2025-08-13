# 🚁 Real-Time Oil Spill Detection with Tello Drone

This project implements a **real-time oil spill detection system** using a **Tello drone** and a custom-trained **YOLOv5** model.  
The drone streams live video via `djitellopy`, and the system processes **2–5 frames per second** to identify oil spills.  
It uses **Python multithreading** to handle video processing and drone control in parallel, ensuring smooth real-time performance without blocking flight commands.  
Upon detection, the drone automatically triggers a **hover command**, allowing immediate response for environmental monitoring.  



# 🛢️ YOLOv5 Oil Spill Detection

Used **YOLOv5** to detect oil spillage in aerial imagery. It was developed using a dataset of nearly **6,000 labeled images** and trained for **real-time deployment** (e.g., drone-based detection).

---

## 🧠 Model Summary

- **Model**: YOLOv5  
- **Framework**: PyTorch + Ultralytics YOLOv5  
- **Training Images**: ~6,000  
- **Training Time**: ~50 epochs

---

## 📊 Performance

Results from training and validation:

- **Precision**: ↑ up to ~0.65  
- **Recall**: ↑ up to ~0.9  
- **mAP@0.5**: ↑ up to ~0.65  
- **Losses**: Gradually decreasing across epochs  

![results curves](https://github.com/user-attachments/assets/54800dfa-67f4-4655-bd85-d171e817a492)

---

## 🚁 Drone Integration

- **Drone Model**: Tello  
- **Control SDK**: [`djitellopy`](https://github.com/damiafuentes/DJITelloPy)  
- Streams live video feed directly into the detection pipeline  
- Processes **2–5 FPS** in real time using YOLOv5 and OpenCV  
- Uses **Python multithreading** to run video processing and drone control in parallel, ensuring smooth real-time performance without blocking flight commands  
- Issues a **hover/stop command** to the drone upon detection  
- Supports **annotated live video view** and **raw feed saving** for analysis

---

## 🎥 Demo
Videos showing oil spill detection in real-time can be found here:
 👉 [result videos] (https://drive.google.com/drive/u/1/folders/1eTG8RwyNfZA0j115slzdCyYajiJ8rK1I) 
 
 ![Screenshot 2025-06-23 183204](https://github.com/user-attachments/assets/e1ce2583-b4ef-4542-80f5-85449d843588) 
![Screenshot 2025-06-23 183251](https://github.com/user-attachments/assets/f079cf3d-6e36-42e0-8caa-24570643decd) 
![Screenshot 2025-06-23 183513](https://github.com/user-attachments/assets/1d40736e-c637-4479-934e-ad1eed7ccb4a)

---


## 🛠️ Installation & Usage

**Clone the official YOLOv5 repository:**

git clone https://github.com/ultralytics/yolov5.git

cd yolov5

**Install dependencies:**

pip install -r requirements.txt

**Clone this repository:**
git clone https://github.com/maryqubty/oil_detection.git

**Change yolo5 path locally:**
go to wrapper_yolo.py and change path

yolov5_path = Path(r"--your own local path--")



## 📦 Dataset
👉 [dataset folder] (https://drive.google.com/drive/u/1/folders/1m--hffO4b3WT3BXbtJwLuKmfP1Ybcq8S).

The dataset is structured into train, valid, and test.

Origin: Custom collected + labeled using Roboflow and existing labeled data from roboflow.

 


## 🧰 Technologies Used

- **Languages & Frameworks**: Python, PyTorch, YOLOv5, OpenCV  
- **Drone Control**: `djitellopy` (Tello SDK)  
- **Concurrency**: Python multithreading for parallel video processing & drone control  
- **Development**: Google Colab (training), Windows (deployment), Git/GitHub  
- **Data Annotation**: LabelImg, Roboflow  
- **Video Processing**: Real-time frame capture, annotation, and saving with OpenCV  


