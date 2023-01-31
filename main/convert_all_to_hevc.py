
from moviepy.editor import *
import os
path="/home/user/yourpath"
def convert_to_hevc(folder_path):
    # Get the list of all files in the folder
    all_files = os.listdir(folder_path)

    # Filter out all files that are not videos
    videos = [f for f in all_files if f.endswith(".mp4") or f.endswith(".avi") or f.endswith(".mkv")]

    # Loop through each video and convert it to HEVC
    for v in videos:
        input_path = os.path.join(folder_path, v)
        output_path = os.path.join(folder_path, v.rsplit(".", 1)[0] + ".hevc")

        # Load the video
        video = VideoFileClip(input_path)

        # Write the video in HEVC format
        video.write_videofile(output_path, codec='libx265')

# Example usage:
convert_to_hevc(f"{path}")
