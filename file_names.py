import os

# individual file to record and print all names of the files so i can use them to generate image links for database
folder_path = 'c:/Users/raman/Desktop/Code-Institute/Milestone-Project-4/media/'

# List all files in the folder
file_names = os.listdir(folder_path)

# Filter out only the files (not directories), not realy needed in my case but usefull code to keep
file_names = [f for f in file_names if os.path.isfile(os.path.join(folder_path, f))]

# Print the list of file names
for file_name in file_names:
    print(file_name)
