from perception import get_frame, preprocess
from obstacle_detection import detect_obstacles
from control import control_decision

VIDEO_PATH = "data/sample_indoor_video.mp4"

frame = get_frame(VIDEO_PATH)
gray = preprocess(frame)
obstacles = detect_obstacles(gray)
decision = control_decision(obstacles)

print("Control Decision:", decision)
