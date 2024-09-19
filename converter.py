import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Define the path to your 'avivideos' folder
folder_path = 'avivideos'

# Get a list of all .AVI files in the folder
avi_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.avi')]
if not avi_files:
    print("No .AVI files found in the folder.")
else:
    clips = [VideoFileClip(file) for file in avi_files]
    final_clip = concatenate_videoclips(clips)

    # Save the final video as .MP4
    final_clip.write_videofile("output.mp4", codec="libx264")

    # Close each clip to release memory
    for clip in clips:
        clip.close()
