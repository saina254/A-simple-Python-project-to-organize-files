import os
import shutil
folder_path = input("Enter folder path to organize: ")
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Others': []
}
for folder in file_types:
    folder_name = os.path.join(folder_path, folder)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    if os.path.isfile(file_path):
        _, extension = os.path.splitext(filename)
        moved = False

        for folder, extensions in file_types.items():
            if extension.lower() in extensions:
                dest_folder = os.path.join(folder_path, folder)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                print(f"Moved: {filename} --> {folder}")
                moved = True
                break
        
        if not moved:
            others_folder = os.path.join(folder_path, 'Others')
            shutil.move(file_path, os.path.join(others_folder, filename))
            print(f"Moved: {filename} --> Others")
