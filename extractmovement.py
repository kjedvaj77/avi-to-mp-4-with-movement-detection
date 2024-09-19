import os
import cv2
from moviepy.editor import VideoFileClip

# Create the folder for saving the clips (in the current project directory)
output_folder = 'movement_clips'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Load the video file
video_path = 'output.mp4'
cap = cv2.VideoCapture(video_path)

# Parameters for movement detection
min_area = 1000
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
warm_up_frames = frame_rate * 2
movement_delay = 5

movement_detected = False
start_frame = 0
movement_segments = []
frame_buffer = []

def detect_movement(frame1, frame2):
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 25, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=2)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > min_area:
            return True
    return False

ret, frame1 = cap.read()
frame_count = 0

while cap.isOpened():
    ret, frame2 = cap.read()
    if not ret:
        break

    if frame_count > warm_up_frames:
        frame_buffer.append(frame2)
        if frame_count % 3 == 0 and len(frame_buffer) > 1:
            if detect_movement(frame_buffer[-2], frame_buffer[-1]):
                if not movement_detected:
                    start_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
                    movement_detected = True
            else:
                if movement_detected and frame_count - start_frame > movement_delay * frame_rate:
                    end_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
                    movement_segments.append((start_frame, end_frame))
                    movement_detected = False

    frame1 = frame2
    frame_count += 1

cap.release()

# Save the movement segments using moviepy
video = VideoFileClip(video_path)
for i, (start, end) in enumerate(movement_segments):
    start_time = start / frame_rate
    end_time = end / frame_rate

    # Create the output file path
    output_path = os.path.join(output_folder, f"movement_clip_{i+1}.mp4")

    # Extract the subclip and save it to the output folder
    subclip = video.subclip(start_time, end_time)
    subclip.write_videofile(output_path, codec="libx264")

print(f"Movement segments saved in folder: {output_folder}")
