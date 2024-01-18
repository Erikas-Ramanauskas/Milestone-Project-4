import os
import re

# Used to convert file names to snake case
# used in a project to rename images to snake case


def convert_to_snake_case(text):
    # Replace hyphens with underscores and use regular expression to convert text to snake case
    text = text.replace(' _', '_')
    # Replace consecutive underscores with a single underscore
    text = re.sub('(_)+', '_', text)
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def rename_files_to_snake_case(folder_path):
    # Check if the provided path is a directory
    if not os.path.isdir(folder_path):
        print(f"{folder_path} is not a valid directory.")
        return

    # List all files in the directory
    files = os.listdir(folder_path)

    # Iterate through each file and rename to snake case
    for file_name in files:
        # Create the new file name by converting to snake case
        new_file_name = convert_to_snake_case(file_name)

        # Construct the full paths for the old and new file names
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {file_name} to {new_file_name}")


if __name__ == "__main__":
    # Replace 'your_folder_path' with the path of the folder containing the files
    folder_path = './readme_images'
    rename_files_to_snake_case(folder_path)
