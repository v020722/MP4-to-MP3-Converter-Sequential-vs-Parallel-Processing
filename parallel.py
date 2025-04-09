import os 
from moviepy.editor import * 
import concurrent.futures 
import time 
def convert_mp4_to_mp3(input_file, output_folder): 
video = VideoFileClip(input_file) 
output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + 
".mp3") 
audio = video.audio 
audio.write_audiofile(output_file) 
print(f"Converted {input_file} to MP3") 
def convert_folder_parallel(input_folder, output_folder): 
    start_time = time.time() 
    with concurrent.futures.ThreadPoolExecutor() as executor:   
    input_files = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if 
    file.endswith(".mp4")] 
    for input_file in input_files: 
    executor.submit(convert_mp4_to_mp3, input_file, output_folder) 
    end_time = time.time()  # Record the end time 
    total_time = end_time - start_time 
print(f"Conversion completed in {total_time} seconds.") 
input_folder ='C:\\Users\\Vijeta\\Desktop\\degree\\computer hardware\\python\\mp4 files' 
output_folder = 'C:\\Users\\Vijeta\\Desktop\\degree\\computer hardware\\python\\results' 
convert_folder_parallel(input_folder, output_folder)