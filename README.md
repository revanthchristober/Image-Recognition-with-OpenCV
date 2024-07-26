# **Image Recognition with OpenCV**

This project demonstrates a simple image recognition system using OpenCV. It includes basic image processing, object detection, and facial recognition techniques.

## Setup Instructions

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/image_recognition_with_opencv.git
cd image_recognition_with_opencv
```

### **2. Create and Activate a Virtual Environment**

#### **On Linux/Mac:**

```bash
python3 -m venv opencv_env
source opencv_env/bin/activate
```

#### **On Windows:**

```bash
python -m venv opencv_env
opencv_env\Scripts\activate
```

### **3. Install Required Libraries**

```bash
pip install -r requirements.txt
```

### **4. Download Required Models**

- Download the `shape_predictor_68_face_landmarks.dat` file from [this link](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2).
- Extract the file and place it in `data/shape_predictors/`.

- Download the Haar cascades XML files from [OpenCV GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades) and place them in `data/haarcascades/`.

## **Running the Project**

### **1. Ensure the Input Images and Templates are in Place**

- Place your input images in `data/input_images/`.
- Place your templates in `data/templates/`.

### **2. Run the Main Script**

```bash
python main.py
```

This will process the images and display the results for various image processing techniques, object detection, and facial recognition.

### **3. View the Output**

The processed images will be saved in `data/output_images/`.

## **Additional Information**

- Modify the `main.py` script to use different input images or templates as needed.
- Refer to the source files in `src/` for detailed implementations of each functionality.

## License

This project is licensed under the GNU 3.0 License. See the [LICENSE](LICENSE) file for more details.
