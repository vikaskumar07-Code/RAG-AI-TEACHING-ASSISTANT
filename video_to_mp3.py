#covert videos to Mp3
import os
import re
import subprocess

Video_folder = "Videos"
Audio_folder="audios"   
files = sorted(os.listdir(Video_folder))
for i, file in enumerate(files, start=1):
    video_path=os.path.join(Video_folder,file)

    name = os.path.splitext(file)[0]
    name = re.sub(r"\[.*?\]", "", name).strip()
    
    audio_path=os.path.join(Audio_folder,f"{name}.mp3")
    print(f"{i}. {name}")
    subprocess.run([ "ffmpeg","-i", video_path,"-vn","-ab", "192k",audio_path])
   