## file-backup-utility
The File Backup Utility is a Python-based tool that allows users to create secure and automated backups of files and directories. It simplifies the backup process, providing an efficient and user-friendly solution for data redundancy.

### Features
- Backup Creation: The utility creates backups of files and directories, preserving the original folder structure.
- Timestamped Backups: Each backup is timestamped with the current date and time, ensuring unique and identifiable backup versions.
Source Folder Selection: Users can specify the source folder from which files and directories need to be backed up.
- Destination Folder Selection: Users can choose the destination folder where the backups will be stored.
- Error Handling: The utility includes error handling to capture and display any errors that occur during the backup process.
- Confirmation Prompt: Users are prompted to confirm before initiating each backup, allowing for user control and preventing accidental backups.
- Interactive Usage: The utility prompts the user to enter the source and destination folders, ensuring a flexible and interactive user experience.

### Requirements
- Python 3.x

### Usage
1. Run the file_backup.py script using Python.
2. When prompted, enter the path of the source folder containing the files and directories to be backed up.
3. Enter the path of the destination folder where the backups will be stored.
Confirm the backup operation when prompted.
4. The utility will create a timestamped backup folder in the destination directory, preserving the original folder structure and copying all files from the source folder.
5. The backup completion message, along with the backup location, will be displayed.

#### Example
```
$ python file_backup.py
Enter the source folder: /path/to/source/folder
Enter the destination folder: /path/to/destination/folder
Do you want to initiate the backup? (yes/no): yes
Backup created successfully.
Backup location: /path/to/destination/folder/backup_20220524150237
```
Please note that the above example assumes that the file_backup.py script is in the same directory as the execution location.

#### Contributing
Contributions to the File Backup Utility project are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

#### License
This project is licensed under the MIT License.