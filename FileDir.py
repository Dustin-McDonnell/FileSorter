import os
import shutil
import tkinter
from tkinter import filedialog
from tkinter import ttk


def user_interface():
    root = tkinter.Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Button(frm, text="Source", command=get_dir).grid(column=1,row=0)
    ttk.Button(frm, text="JPG Destination", command=get_dir).grid(column=1, row=1)
    root.protocol('WM_DELETE_WINDOW')
    root.mainloop()


def get_dir():
    dir_name = filedialog.askdirectory()
    return dir_name


def list_dir(dir_name):
    return [os.path.join(dir_name, file) for file in os.listdir(dir_name)]


def move_files(dir_list, path):
    for file in dir_list:
        if file.endswith('.jpg'):
            shutil.move(file, path)


def run():
    #dir_name = get_dir()
    #dest_name = get_dir()
    #dir_list = list_dir(dir_name)
    #move_files(dir_list,dest_name)
    user_interface()

