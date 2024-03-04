
import requests
import moviepy.editor as mp
import tempfile

# URL of the video
video_url = "https://media-lib.freshlearn.com/7373/Azure+Data+Engineering+Session+14+%282022-12-18+10_55+GMT%2B5_30%29-U0S4PiqFHw.mp4"

# Fetch the video content
response = requests.get(video_url)
video_content = response.content

# Save the content to a temporary file
with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp_file:
    temp_file.write(video_content)
    temp_file_path = temp_file.name

# Convert video to audio
clip = mp.VideoFileClip(temp_file_path)
clip.audio.write_audiofile("output2_audio.mp3")

# Clean up temporary file
import os
os.remove(temp_file_path)
