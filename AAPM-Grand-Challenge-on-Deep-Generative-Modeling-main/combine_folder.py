import os
import shutil

# Define the source folder path where items are scattered
source_folder = '/Users/alokroy/Downloads/challenge_data '

# Define the destination folder path where items will be merged
destination_folder = '/Users/alokroy/Desktop/Images'

# Get a list of all items in the source folder
all_items = os.listdir(source_folder)

# Iterate through each item in the source folder
for item in all_items:
    source_item_path = os.path.join(source_folder, item)

    # If the item is a file, move it to the destination folder
    if os.path.isfile(source_item_path):
        destination_item_path = os.path.join(destination_folder, item)
        
        # If the item with the same name already exists in the destination folder,
        # rename the item in the source folder before moving it
        if os.path.exists(destination_item_path):
            base_name, extension = os.path.splitext(item)
            i = 1
            while os.path.exists(destination_item_path):
                new_item_name = f"{base_name}_{i}{extension}"
                destination_item_path = os.path.join(destination_folder, new_item_name)
                i += 1
        
        shutil.move(source_item_path, destination_item_path)
    # If the item is a folder, merge it recursively with the destination folder
    elif os.path.isdir(source_item_path):
        folder_items = os.listdir(source_item_path)
        for folder_item in folder_items:
            source_folder_item_path = os.path.join(source_item_path, folder_item)
            destination_folder_item_path = os.path.join(destination_folder, folder_item)
            
            # If the item with the same name already exists in the destination folder,
            # rename the item in the source folder before moving it
            if os.path.exists(destination_folder_item_path):
                base_name, extension = os.path.splitext(folder_item)
                i = 1
                while os.path.exists(destination_folder_item_path):
                    new_folder_item_name = f"{base_name}_{i}{extension}"
                    destination_folder_item_path = os.path.join(destination_folder, new_folder_item_name)
                    i += 1
            
            shutil.move(source_folder_item_path, destination_folder_item_path)

print('Items inside multiple folders combined successfully into one folder!')
