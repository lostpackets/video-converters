from moviepy.editor import *
import os

path="/home/user/testfolder"

def combine_videos(folder_path):
    # Get the list of all files in the folder
    all_files = os.listdir(folder_path)

    # Filter out all files that are not videos
    videos = [f for f in all_files if f.endswith(".mp4") or f.endswith(".avi") or f.endswith(".mkv")]

    # Combine the videos
    final_video = concatenate_videoclips([VideoFileClip(os.path.join(folder_path, v)) for v in videos])

    # Write the final video to disk
    final_video.write_videofile("final_video.mp4")

# Example usage:
combine_videos(f"{path}")
