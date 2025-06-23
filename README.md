# 🛢️ YOLOv5 Oil Spill Detection

This project uses **YOLOv5** to detect oil spillage in aerial imagery. It was developed using a dataset of nearly **6,000 labeled images** and trained for **real-time deployment** (e.g., drone-based detection).

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

## 🛠️ Installation & Usage

# Clone the official YOLOv5 repository
git clone https://github.com/ultralytics/yolov5.git
cd yolov5

# Install dependencies
pip install -r requirements.txt

# Run detection using the trained model
python detect.py --weights /path/to/your_repo/weights/best.pt --source /path/to/video_or_image


## 📦 Dataset
The dataset is structured into train, valid, and test.

Format: YOLO TXT annotations.

Origin: Custom collected + labeled using Roboflow and existing labeled data from roboflow.

For more info, check README.dataset.txt and README.roboflow.txt.
# 👉 [dataset folder] (https://drive.google.com/drive/u/1/folders/1m--hffO4b3WT3BXbtJwLuKmfP1Ybcq8S)

🎥 Demo
Videos showing oil spill detection in real-time can be found here:
# 👉 [result videos] (https://drive.google.com/drive/u/1/folders/1eTG8RwyNfZA0j115slzdCyYajiJ8rK1I) 

🤖 Future Work
Integrate real-time video feed from DJI Mini 3 Pro

Trigger drone to stop/freeze upon detection

Add environmental variation to dataset (waves, light, water color)

