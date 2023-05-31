import pytube
from moviepy.editor import *
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
import pytube
import speech_recognition as sr
import youtube_transcript_api
import time




# Get the video URL from the user.
link = input("Enter the YouTube video link: ")

# Create a YouTube object using the provided link.
youtube = pytube.YouTube(link)

# Select the highest resolution video stream available.
video_stream = youtube.streams.get_highest_resolution()

# Set the output directory path.
output_dir_path = "Insert folder one path here"

# Download the video to the output directory path.
if video_stream:
    video_stream.download(output_dir_path)







# Get the transcript of the YouTube video with the provided video ID.
def get_transcript(video_id):
    transcript = youtube_transcript_api.YouTubeTranscriptApi.get_transcript(video_id)
    text = ""
    for line in transcript:
        text += line['text'] + " "
    return text

# Get the video ID from the YouTube link.
def get_video_id(link):
    video_id = link.split("v=")[1]
    return video_id

# Get the YouTube link from the user.


# Get the transcript of the YouTube video.
video_id = get_video_id(link)
transcript = get_transcript(video_id)
print("GET READY FOR PROMPT")


# Add "hello world" to the beginning of the transcript.
transcript = "Hello AI I would like you to help me find out which 59 second clip from this youtube transcript would work best, you must judge out of this entire transcript where 59 seoncds starts and where it ends, this marks one clip. so every time this happens you know this is part one, then part tow then part three etc. You must look at these clips and tell the user with quoted examples which one is the best and which one is best for youtube. you must also answer the number of the chronilogical clip Ex: (script) answer yes, clip 4 is the best (quote) also list the part number. " + transcript

time.sleep(10)

# Print the transcript.
print(transcript)

time.sleep(10)

    






        

input_dir = r"insert folder one path here"
output_dir = r"insert folder two path here"

# Find the first .mp4 file in the input directory
input_file = next((os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(".mp4")), None)

if input_file is None:
    print("No .mp4 files found in input directory")
else:
    # Use ffmpeg to crop the video to a 9:16 aspect ratio
    os.system(f'ffmpeg -i "{input_file}" -filter:v "crop=in_h*9/16:in_h" -c:a copy "{os.path.join(output_dir, os.path.basename(input_file))}"')
    print("Video cropped and saved to output directory")


    input_dir = r"insert folder two path here"
output_dir = r"insert folder three path here"

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




