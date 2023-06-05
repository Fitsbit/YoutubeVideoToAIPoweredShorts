import pytube
from moviepy.editor import *
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
import speech_recognition as sr
import youtube_transcript_api
import time
input_dir = r"insert path one"
output_dir = r"insert path two"

#I get it with the imports but i just copy and pasted so...

# Find the first .mp4 file in the input directory
input_file = next((os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(".mp4")), None)

if input_file is None:
    print("No .mp4 files found in input directory")
else:
    # Use ffmpeg to crop the video to a 9:16 aspect ratio
    os.system(f'ffmpeg -i "{input_file}" -filter:v "crop=in_h*9/16:in_h" -c:a copy "{os.path.join(output_dir, os.path.basename(input_file))}"')
    print("Video cropped and saved to output directory")


    input_dir = r"insert path two"
output_dir = r"insert path three"

# Find all .mp4 files in the input directory
input_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(".mp4")]

if not input_files:
    print("No .mp4 files found in input directory")
else:
    for input_file in input_files:
        # Load the video file using moviepy
        video = VideoFileClip(input_file)

        # Calculate the number of 59-second clips in the video
        num_clips = int(video.duration // 59)

        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Iterate over each clip and save it to the output directory
        for i in range(num_clips):
            start_time = i * 59
            end_time = min((i + 1) * 59, video.duration)
            clip = video.subclip(start_time, end_time)
            output_file_path = os.path.join(output_dir, f"{i+1}.mp4")
            clip.write_videofile(output_file_path)

        # Close the video file
        video.close()

    print("Videos cropped and saved to output directory")
