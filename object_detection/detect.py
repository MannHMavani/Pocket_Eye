import cv2
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("object_detection/yolov8m.pt")  # or yolov8n.pt for faster performance
names = model.names  # COCO class names

def detect_webcam(speak_callback):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Webcam not detected.")
        return

    print("✅ Webcam started. Press 'q' to quit.")

    spoken_labels = set()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame.")
            break

        results = model(frame)
        labels = set()

        for result in results:
            for box in result.boxes:
                cls = int(box.cls[0])
                label = names[cls]
                labels.add(label)

        for label in labels:
            if label not in spoken_labels:
                print(f"🧠 Detected: {label}")
                speak_callback(f"{label}")
                spoken_labels.add(label)

        cv2.imshow("PocketEye – Live Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("📴 Exiting...")
            break

    cap.release()
    cv2.destroyAllWindows()
