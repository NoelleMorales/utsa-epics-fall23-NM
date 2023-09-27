import os
import shutil

folder_path = "C:\\Users\\Rosie\\OneDrive\\Desktop\\EPICS Pic"
image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

script_filename = os.path.basename(__file__)

for index, filename in enumerate(image_files, start=1):
    name, extension = os.path.splitext(filename)
    
    # Skip renaming the script file itself and other Python files nm = noelle morales
    if filename != script_filename and extension.lower() not in ['.py', '.pyc', '.pyo']:
        new_filename = f"rosie_{index:02d}{extension}"

        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)

        shutil.move(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")
    
print("Renaming completed.")
