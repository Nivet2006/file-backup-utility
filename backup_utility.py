import os
import shutil
import datetime

def backup_files():
    print("Welcome to the Python Folder Backup utility")
    source_folder = input("Enter the source folder: ")

    if not os.path.exists(source_folder):
        print("Source folder does not exist.")
        return

    destination_folder = input("Enter the destination folder: ")

    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        backup_folder = os.path.join(destination_folder, f"backup_{timestamp}")

        os.makedirs(backup_folder)

        for root, dirs, files in os.walk(source_folder):
            for file in files:
                source_path = os.path.join(root, file)
                destination_path = os.path.join(backup_folder, os.path.relpath(source_path, source_folder))
                shutil.copy2(source_path, destination_path)

        print("Backup created successfully.")
        print("Backup location:", backup_folder)

    except OSError as e:
        print("Error:", e)

backup_files()

while True:
    user_input = input("Do you want to perform another backup? (yes/no): ")
    if user_input.lower() == "yes":
        backup_files()
    elif user_input.lower() == "no":
        print("Thank you for using Python Folder Backup utility")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
