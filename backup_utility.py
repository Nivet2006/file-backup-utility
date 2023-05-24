import os
import shutil
import datetime

def backup_files():
    # Prompt the user to enter the source folder
    source_folder = input("Enter the source folder: ")

    # Verify that the source folder exists
    if not os.path.exists(source_folder):
        print("Source folder does not exist.")
        return

    # Prompt the user to enter the destination folder
    destination_folder = input("Enter the destination folder: ")

    try:
        # Create a timestamp for the backup folder name
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        backup_folder = os.path.join(destination_folder, f"backup_{timestamp}")

        # Create the backup folder
        os.makedirs(backup_folder)

        # Walk through the source folder and copy files to the backup folder
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                source_path = os.path.join(root, file)
                destination_path = os.path.join(backup_folder, os.path.relpath(source_path, source_folder))
                shutil.copy2(source_path, destination_path)

        print("Backup created successfully.")
        print("Backup location:", backup_folder)

    except OSError as e:
        print("Error:", e)

# Run the backup_files function
backup_files()

# Prompt the user for confirmation to continue
while True:
    user_input = input("Do you want to perform another backup? (yes/no): ")
    if user_input.lower() == "yes":
        backup_files()
    elif user_input.lower() == "no":
        print("Thank you for using Python Folder Backup utility")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
