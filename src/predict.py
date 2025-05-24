import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load your saved model (change filename if needed)
model = load_model('lazy_landmark_model.h5')

# Define the classes exactly as in your training folders
classes = ['eiffel_tower', 'statue_of_liberty']  # update with your class names

def predict(image_path):
    # Read image using OpenCV
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to load image {image_path}")
        return

    # Resize image to model input size (224x224)
    img_resized = cv2.resize(img, (224, 224))

    # Normalize pixels to [0,1]
    x = img_resized.astype('float32') / 255.0

    # Add batch dimension: (1, 224, 224, 3)
    x = np.expand_dims(x, axis=0)

    # Run prediction
    preds = model.predict(x)[0]  # model.predict returns a batch; take first result

    # Get index of max confidence and the confidence value
    idx = np.argmax(preds)
    label = classes[idx]
    prob = preds[idx]

    # Overlay label and confidence on original image
    cv2.putText(img, f"{label}: {prob:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the image with prediction
    cv2.imshow('Prediction', img)
    cv2.waitKey(0)  # Wait for key press to close window
    cv2.destroyAllWindows()

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python src/predict.py <image_path>")
    else:
        predict(sys.argv[1])
