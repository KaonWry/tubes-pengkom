# Packages
import datetime
from datetime import timedelta
from tkinter import *
from barcode import EAN13
from barcode.writer import ImageWriter
import re
import inquirer
import os


# TUI pintu masuk 
def pintuMasuk():
    menuPintuMasuk = [
        inquirer.List
        (
            "Tipe Kendaraan", 
            message = "Masukan tipe kendaraan", 
            choices = ["Mobil", "Motor", "Truk/Bus"],
        ),
        inquirer.Text
        (
            "Plat Nomor",
            message = "Masukan plat nomor kendaraan",
            validate = lambda _, x: re.match('[a-zA-Z]+\s+[0-9]+\s+[a-zA-Z]+', x),
        ),
        inquirer.Confirm
        (
            "Kartu Member",
            message = "Apakah ada kartu member?",
        ),
        inquirer.Text
        (
            "Waktu Masuk",
            message = "Masukan jam dan menit masuk dalam format HH:MM:SS DD/MM",
            validate = lambda _, x: re.match('[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{1,3})?\s+(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|[1][0-2])', x),
        ),
    ]
    menuPintuMasuk = inquirer.prompt(menuPintuMasuk)
    

# TUI pintu keluar
def pintuKeluar():
    menuPintuKeluar = [
        inquirer.Text
        (
            "Barcode",
            message = "Masukan barcode pintu masuk",
        ),
        inquirer.Text
        (
            "Pembayaran",
            message = "Masukan nominal pembayaran",
            validate = lambda _, x: re.match ('[0-9]+', x),
        ),
    ]
    menuPintuKeluar = inquirer.prompt(menuPintuKeluar)
   

# Bersihkan halaman terminal
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

    
# TUI menu utama
mainMenu = [
    inquirer.List
    (
        "menuSelection",
        message="Pilih menu",
        choices=["Pintu Masuk", "Pintu Keluar", "Keluar"],
    ),
]

while True:
    menu = inquirer.prompt(mainMenu)
    if (menu["menuSelection"] == "Pintu Masuk"):
        pintuMasuk()
    elif (menu["menuSelection"] == "Pintu Keluar"):
        pintuKeluar()
    elif (menu["menuSelection"] == "Keluar"):
       exit()