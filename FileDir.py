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
    print(os.listdir(dir_name))


def run():
    dir_name = get_dir()
    list_dir(dir_name)