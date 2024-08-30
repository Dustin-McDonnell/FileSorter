import os
import shutil
import tkinter
from tkinter import filedialog


def get_dir():
    root = tkinter.Tk()
    root.withdraw()
    dir_name = filedialog.askdirectory()
    return dir_name


def list_dir(dir_name):
    return [os.path.join(dir_name, file) for file in os.listdir(dir_name)]


def move_files(dir_list, path):
    for file in dir_list:
        if file.endswith('.jpg'):
            shutil.move(file, path)


def run():
    dir_name = get_dir()
    dest_name = get_dir()
    dir_list = list_dir(dir_name)
    move_files(dir_list,dest_name)

