# Packages
import datetime
from datetime import timedelta
from tkinter import *
from barcode import EAN13
from barcode.writer import ImageWriter
import re
import inquirer

# Input data
while True:
    menu = [
        inquirer.List
        (
            "menuSelection",
            message="Pilih menu",
            choices=["Pintu Masuk", "Pintu Keluar", "Keluar"],
        ),
    ]
    menu = inquirer.prompt(menu)
    if (menu == "Keluar"):
        break
    elif (menu == "Pintu Masuk"):
        pintuMasuk()
    elif (menu == "PINtu Keluar"):
        pintuKeluar()


# TUI pintu masuk 
def pintuMasuk():
    
    

# TUI pintu keluar
def pintuKeluar():
    