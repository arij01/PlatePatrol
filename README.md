# automatic-number-plate-recognition

https://github.com/user-attachments/assets/8551d49c-a361-4bf1-b01e-b2fe9fd7bf5e

## Description 

## Data
The video I used in this tutorial can be downloaded [here](https://www.pexels.com/video/traffic-flow-in-the-highway-2103099/).

## Model
A Yolov8 pre-trained model (YOLOv8n) was used to detect vehicles.

A licensed plate detector was used to detect license plates. The model was trained with Yolov8 using this [dataset](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4).

## Dependencies
The sort module needs to be downloaded from this [repository](https://github.com/abewley/sort).

## Installation  
To get started, follow these steps:  

1. **Clone the repository:**  
   ```bash  
   git clone https://github.com/arij01/automatic-number-plate-recognition.git
2. **Navigate to the project directory:**
   ```bash
   cd automatic-number-plate-recognition
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Run main.py:**
      ```bash
   python main.py
5. **Run the add_missing_data.py file:**
      ```bash
   python add_missing_data.py
6. **Run the visualize.py file:**
      ```bash
   python visualize.py
