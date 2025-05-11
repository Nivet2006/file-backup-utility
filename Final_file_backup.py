import os
import shutil
import datetime
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pyzipper
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
except ImportError:
    messagebox.showerror("Missing Package", "Install 'tkinterdnd2' via pip:\npip install tkinterdnd2")
    exit()

class BackupApp:
    def __init__(self, root):
        self.root = root
        self.style = ttkb.Style()
        self.theme = "darkly"
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Advanced File Backup Utility")
        self.root.geometry("500x450")

        # Theme toggle
        self.theme_toggle = ttkb.Checkbutton(self.root, text="Toggle Light/Dark Mode", bootstyle="info", command=self.toggle_theme)
        self.theme_toggle.pack(pady=10)

        # Source folder with drag-and-drop
        ttkb.Label(self.root, text="Source Folder:").pack(pady=5)
        self.source_entry = ttkb.Entry(self.root, width=60)
        self.source_entry.pack()
        self.source_entry.drop_target_register(DND_FILES)
        self.source_entry.dnd_bind('<<Drop>>', self.handle_drop_source)
        ttkb.Button(self.root, text="Browse", command=self.browse_source, bootstyle="secondary-outline").pack(pady=5)

        # Destination folder
        ttkb.Label(self.root, text="Destination Folder:").pack(pady=5)
        self.dest_entry = ttkb.Entry(self.root, width=60)
        self.dest_entry.pack()
        ttkb.Button(self.root, text="Browse", command=self.browse_destination, bootstyle="secondary-outline").pack(pady=5)

        # File types to include
        ttkb.Label(self.root, text="Include File Types (e.g. .pdf,.docx,.jpg):").pack(pady=5)
        self.file_types_entry = ttkb.Entry(self.root, width=60)
        self.file_types_entry.pack()

        # Zip password
        ttkb.Label(self.root, text="Zip Password (Optional):").pack(pady=5)
        self.password_entry = ttkb.Entry(self.root, show="*", width=60)
        self.password_entry.pack()

        # Progress bar
        self.progress = ttkb.Progressbar(self.root, length=400)
        self.progress.pack(pady=10)

        # Backup button
        ttkb.Button(self.root, text="Create Backup", bootstyle="success", command=self.start_backup).pack(pady=20)

    def toggle_theme(self):
        self.theme = "flatly" if self.theme == "darkly" else "darkly"
        self.style.theme_use(self.theme)

    def handle_drop_source(self, event):
        path = event.data.strip('{}')
        if os.path.isdir(path):
            self.source_entry.delete(0, tk.END)
            self.source_entry.insert(0, path)

    def browse_source(self):
        folder = filedialog.askdirectory()
        self.source_entry.delete(0, tk.END)
        self.source_entry.insert(0, folder)

    def browse_destination(self):
        folder = filedialog.askdirectory()
        self.dest_entry.delete(0, tk.END)
        self.dest_entry.insert(0, folder)

    def start_backup(self):
        threading.Thread(target=self.backup_files).start()

    def backup_files(self):
        source = self.source_entry.get()
        dest = self.dest_entry.get()
        include_types = self.file_types_entry.get().split(',')
        password = self.password_entry.get()

        if not os.path.exists(source) or not os.path.exists(dest):
            messagebox.showerror("Error", "Check source and destination paths.")
            return

        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        zip_path = os.path.join(dest, f"backup_{timestamp}.zip")

        try:
            files_to_backup = []
            for root, _, files in os.walk(source):
                for file in files:
                    if not include_types or any(file.endswith(ext.strip()) for ext in include_types):
                        full_path = os.path.join(root, file)
                        arcname = os.path.relpath(full_path, source)
                        files_to_backup.append((full_path, arcname))

            self.progress.config(maximum=len(files_to_backup))
            self.progress["value"] = 0

            with pyzipper.AESZipFile(zip_path, 'w', compression=pyzipper.ZIP_DEFLATED) as zf:
                if password:
                    zf.setpassword(password.encode())
                    zf.setencryption(pyzipper.WZ_AES, nbits=256)
                for i, (src, arcname) in enumerate(files_to_backup):
                    zf.write(src, arcname)
                    self.progress.step()
                    self.root.update_idletasks()

            messagebox.showinfo("Success", f"Backup completed!\nSaved to: {zip_path}")

        except Exception as e:
            messagebox.showerror("Backup Failed", str(e))

if __name__ == '__main__':
    root = TkinterDnD.Tk()
    ttkb.Style("darkly")
    app = BackupApp(root)
    root.mainloop()
