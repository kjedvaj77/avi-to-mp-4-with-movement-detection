import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
from datetime import datetime

# Function to get folder creation time (fallback to folder modification time if creation time is not available)
def get_folder_creation_time(folder_path):
    return os.path.getctime(folder_path)

# Function to find all .avi files in a folder and its subfolders
def find_avi_files_with_dates(base_folder):
    avi_files_with_dates = []

    # Traverse through the base folder and all subfolders
    for root, dirs, files in os.walk(base_folder):
        folder_creation_time = get_folder_creation_time(root)
        
        # Find all .avi files and get their creation time
        for file in files:
            if file.endswith('.avi'):
                file_path = os.path.join(root, file)
                file_creation_time = os.path.getctime(file_path)
                avi_files_with_dates.append((file_path, folder_creation_time, file_creation_time))

    return avi_files_with_dates

# Ask user for the folder path containing .AVI videos
folder_path = input("Enter the path to the folder containing .AVI videos: ")

# Expand user path (~) and get absolute path
folder_path = os.path.abspath(os.path.expanduser(folder_path))

# Check if the folder exists
if not os.path.exists(folder_path):
    print(f"The folder '{folder_path}' does not exist.")
else:
    # Find all .avi files, including in subfolders, with their folder and file creation times
    avi_files = find_avi_files_with_dates(folder_path)

    # Sort first by folder creation date, then by file creation date
    avi_files.sort(key=lambda x: (x[1], x[2]))

    # Check if any .avi files were found
    if not avi_files:
        print("No .AVI files found in the folder or its subfolders.")
    else:
        # Load and concatenate video clips
        clips = [VideoFileClip(file[0]) for file in avi_files]
        final_clip = concatenate_videoclips(clips)

        # Ask user for output filename
        output_filename = input("Enter the output filename (without extension): ") + ".mp4"
        
        # Save the final video as .MP4
        final_clip.write_videofile(output_filename, codec="libx264")

        # Close each clip to release memory
        for clip in clips:
            clip.close()

        print(f"Video saved as {output_filename}")
