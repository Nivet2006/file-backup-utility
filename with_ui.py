import os
import shutil
import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to perform backup
def backup_files():
    source_folder = source_entry.get()
    destination_folder = dest_entry.get()

    if not os.path.exists(source_folder):
        messagebox.showerror("Error", "Source folder does not exist.")
        return

    if not os.path.exists(destination_folder):
        messagebox.showerror("Error", "Destination folder does not exist.")
        return

    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        backup_folder = os.path.join(destination_folder, f"backup_{timestamp}")
        os.makedirs(backup_folder)

        for root, _, files in os.walk(source_folder):
            for file in files:
                src_file = os.path.join(root, file)
                rel_path = os.path.relpath(src_file, source_folder)
                dest_file = os.path.join(backup_folder, rel_path)

                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                shutil.copy2(src_file, dest_file)

        messagebox.showinfo("Success", f"Backup created successfully!\nLocation: {backup_folder}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Browse functions
def browse_source():
    folder = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, folder)

def browse_destination():
    folder = filedialog.askdirectory()
    dest_entry.delete(0, tk.END)
    dest_entry.insert(0, folder)

# Setup GUI
root = tk.Tk()
root.title("File Backup Utility")
root.geometry("500x300")
root.configure(bg="#2d0036")

# Labels
tk.Label(root, text="Source Folder:", bg="#2d0036", fg="white", font=("Segoe UI", 11)).pack(pady=5)
source_entry = tk.Entry(root, width=50, font=("Segoe UI", 10))
source_entry.pack()
tk.Button(root, text="Browse", command=browse_source, bg="#6a0dad", fg="white").pack(pady=5)

tk.Label(root, text="Destination Folder:", bg="#2d0036", fg="white", font=("Segoe UI", 11)).pack(pady=5)
dest_entry = tk.Entry(root, width=50, font=("Segoe UI", 10))
dest_entry.pack()
tk.Button(root, text="Browse", command=browse_destination, bg="#6a0dad", fg="white").pack(pady=5)

# Backup Button
tk.Button(root, text="Backup Now", command=backup_files, font=("Segoe UI", 12, "bold"),
          bg="#a020f0", fg="white", padx=20, pady=5).pack(pady=20)

# Run the GUI
root.mainloop()
