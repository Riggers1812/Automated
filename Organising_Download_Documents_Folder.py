from datetime import datetime
from pathlib import Path
import os

# Create a path object
my_files = Path(r"C:\Users\dtrig\Downloads\Documents")

# Is the path a file?
print(my_files.is_file())  # Returns false

# Is the path a directory?
print(my_files.is_dir())  # Returns true

# What is the parent of the file?
print(my_files.parent)  # Returns C:\Users\dtrig

# What is the base of the filename?
print(my_files.stem)  # Returns Files

# What are the extensions of the file?
print(my_files.suffix)  # Returns "" (since it's not a file)

for file in my_files.iterdir():
    print(file)


# Sets which Folder contains what file types
folder_names = {
    "Data": {"csv"},
    "Excel": {"xls", "xlsb", "xlsx"},
    "Pdfs": {"pdf", "epub"},
    "Word": {"doc", "docx"},
    "Others": {"NONE"},
}

# Extract list of files/folders
onlyfiles = [
    os.path.join(my_files, file)
    for file in os.listdir(my_files)
    if os.path.isfile(os.path.join(my_files, file))
]

onlyfolders = [
    os.path.join(my_files, file)
    for file in os.listdir(my_files)
    if not os.path.isfile(os.path.join(my_files, file))
]

extension_filetype_map = {
    extension: fileType
    for fileType, extensions in folder_names.items()
    for extension in extensions
}

# make folders
folder_paths = [
    os.path.join(my_files, folder_name) for folder_name in folder_names.keys()
]

[os.mkdir(folderPath) for folderPath in folder_paths if not os.path.exists(folderPath)]


# move files
def new_path(old_path):
    extension = str(old_path).split(".")[-1]
    amplified_folder = (
        extension_filetype_map[extension]
        if extension in extension_filetype_map.keys()
        else "Others"
    )
    final_path = os.path.join(my_files, amplified_folder, str(old_path).split("\\")[-1])
    return final_path


[Path(eachfile).rename(new_path(eachfile)) for eachfile in onlyfiles]

# Move other folders
[
    Path(onlyfolder).rename(
        os.path.join(my_files, "Others", str(onlyfolder).split("\\")[-1])
    )
    for onlyfolder in onlyfolders
    if str(onlyfolder).split("\\")[-1] not in folder_names.keys()
]
