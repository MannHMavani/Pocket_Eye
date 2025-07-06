from object_detection.detect import detect_webcam
from tts.speak import speak

if __name__ == "__main__":
    print("📦 PocketEye Phase 2: Live Detection")
    detect_webcam(speak_callback=speak)
