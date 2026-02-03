import cv2

def detect_obstacles(gray_frame):
    edges = cv2.Canny(gray_frame, 50, 150)
    return edges
