import os 
from moviepy.editor import VideoFileClip 
import time   
 
def convert_mp4_to_mp3(input_file, output_folder): 
    try: 
        video = VideoFileClip(input_file) 
        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + 
".mp3") 
        audio = video.audio 
        
 
        audio.write_audiofile(output_file) 
        video.close() 
        audio.close() 
        return True, f"Conversion of {input_file} completed successfully" 
    except Exception as e: 
        return False, f"Error converting {input_file}: {str(e)}" 
 
def convert_folder_sequential(input_folder, output_folder): 
    log_file = os.path.join(output_folder, "conversion_log.txt") 
    start_time = time.time()  
    with open(log_file, "w") as log: 
        input_files = [file for file in os.listdir(input_folder) if file.endswith(".mp4")] 
        total_files = len(input_files) 
        completed_files = 0 
        for input_file in input_files: 
            success, message = convert_mp4_to_mp3(os.path.join(input_folder, input_file), 
output_folder) 
            if success: 
                completed_files += 1 
            log.write(message + "\n") 
print(f"Processed {input_file}. {completed_files}/{total_files} completed.") 
end_time = time.time()   
total_time = end_time - start_time 
log.write(f"Conversion completed in {total_time} seconds.\n") 
print(f"Conversion completed for all files. Check {log_file} for details.") 
print(f"Total time taken for conversion: {total_time} seconds.") 
input_folder = 'C:\\Users\\Vijeta\\Desktop\\degree\\computer hardware\\python\\mp4 files' 
output_folder = 'C:\\Users\\Vijeta\\Desktop\\degree\\computer hardware\\python\\results'  
convert_folder_sequential(input_folder, output_folder)