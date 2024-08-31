import os
import shutil
import tkinter
from tkinter import *
import json
from tkinter import ttk, filedialog

CONFIG_FILE = 'config.json'


# Load paths from the config file. If the file doesn't exist, create a default config.
def load_paths():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    else:
        default_config()
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)


# Create a default configuration file with empty paths.
def default_config():
    with open(CONFIG_FILE, 'w') as f:
        json.dump({"jpg": "", "png": "", "gif": "", "jpeg": "",
                   "xlsx": "", "docx": "", "mp4": "", "pdf": "", "webp": "", "src": ""}, f, indent=4)


# Save the selected directory path for the given file extension.
def save_paths(extension, paths):
    path = get_dir()
    if path:
        paths[extension] = path
        with open(CONFIG_FILE, 'w') as f:
            json.dump(paths, f, indent=4)


# Create buttons for each file extension and add them to the frame.
def create_buttons(frm, paths):
    button_config = {
        "JPG Destination": "jpg",
        "PNG Destination": "png",
        "GIF Destination": "gif",
        "JPEG Destination": "jpeg",
        "XLSX Destination": "xlsx",
        "DOCX Destination": "docx",
        "MP4 Destination": "mp4",
        "PDF Destination": "pdf",
        "WEBP Destination": "webp"
    }

    for i, (button, extension) in enumerate(button_config.items()):
        ttk.Button(frm, text=button, command=lambda ext=extension: save_paths(ext, paths)).grid(column=1 + i, row=1)


# Set up the user interface with buttons and start the main loop.
def user_interface():
    root = tkinter.Tk()
    frm = ttk.Frame(root, padding=10)
    root.title('File Auto Sorter')
    paths = load_paths()
    frm.grid()
    ttk.Button(frm, text="Source", command=lambda: save_paths("src", paths)).grid(column=1, row=0)
    create_buttons(frm, paths)
    ttk.Button(frm, text="Run", command=lambda: move_files(paths)).grid(column=1, row=2)
    root.protocol('WM_DELETE_WINDOW')
    root.mainloop()


# Open a directory selection dialog and return the selected directory path.
def get_dir():
    dir_name = filedialog.askdirectory()
    return dir_name


# List all files in the given directory.
def list_dir(dir_name):
    return [os.path.join(dir_name, file) for file in os.listdir(dir_name)]


# Move files with a .jpg extension to the specified path.
def move_files(paths):
    src_files = list_dir(paths['src'])

    extensions = {
        '.jpg': paths['jpg'],
        '.png': paths['png'],
        '.gif': paths['gif'],
        '.jpeg': paths['jpeg'],
        '.xlsx': paths['xlsx'],
        '.docx': paths['docx'],
        '.mp4': paths['mp4'],
        '.pdf': paths['pdf'],
        '.webp': paths['webp']
    }

    for file in src_files:
        for ext, dest in extensions.items():
            if file.endswith(ext):
                shutil.move(file, dest)
                break


# Run the application by starting the user interface.
def run():
    user_interface()
