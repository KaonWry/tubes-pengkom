# Packages
import datetime as dt
from datetime import date, timedelta
import datetime
import time
from tkinter import *
from barcode import EAN13
from barcode.writer import ImageWriter
import re
import inquirer
import os
from random import seed
from random import randint
seed(1)


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
            message = "Masukan jam dan menit masuk dalam format DD-MM-YYYY HH:MM:SS",
            validate = lambda _, x: re.match('(0?[1-9]|[12][0-9]|3[01])-(0?[1-9]|[1][0-2])-[0-9]+\s+[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{1,3})?', x),
        ),
    ]
    menuPintuMasuk = inquirer.prompt(menuPintuMasuk)
    
    # Tipe kendaraan
    if(menuPintuMasuk["Tipe Kendaraan"] == "Mobil"):
        tipeKendaraan = str("1")
    elif(menuPintuMasuk["Tipe Kendaraan"] == "Motor"):
        tipeKendaraan = str("2")
    elif(menuPintuMasuk["Tipe Kendaraan"] == "Truk/Bus"):
        tipeKendaraan = str("3")
        
    # Plat nomor
    platNomor = (menuPintuMasuk["Plat Nomor"].replace(" ", "")).upper()
    
    # Waktu masuk
    waktu = [0] * 2
    waktu = menuPintuMasuk["Waktu Masuk"].split(" ")
    pukul = [0] * 3
    pukul = waktu[0]
    pukul = pukul.split(":")
    pukul = (((pukul[0]*60)+pukul[1])*60)+pukul[2]
    tanggal = waktu[1]
    tanggal = time.mktime(datetime.datetime.strptime(tanggal, "%d/%m/%Y").timetuple())
    
    print(pukul, tanggal, pukul + tanggal)
    
    # Membership
    if(menuPintuMasuk["Kartu Member"]):
        member = "Y"
    else:
        member = "N"
        
    # Angka random pengaman
    for i in range(3):
        random += randint(0,9)
    
    
    

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