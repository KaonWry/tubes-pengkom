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

# Bersihkan halaman terminal
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

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
        tipeKendaraan = str("MB")
    elif(menuPintuMasuk["Tipe Kendaraan"] == "Motor"):
        tipeKendaraan = str("MT")
    elif(menuPintuMasuk["Tipe Kendaraan"] == "Truk/Bus"):
        tipeKendaraan = str("TR")
        
    # Plat nomor
    platNomor = (menuPintuMasuk["Plat Nomor"].replace(" ", "")).upper()
    
    # Waktu masuk
    waktu = [0] * 2
    waktu = menuPintuMasuk["Waktu Masuk"].split(" ")
    pukul = [0] * 3
    pukul = waktu[1]
    pukul = pukul.split(":")
    pukul = (((int(pukul[0])*60)+int(pukul[1]))*60)+int(pukul[2])
    tanggal = waktu[0]
    tanggal = int(time.mktime(datetime.datetime.strptime(tanggal, "%d-%m-%Y").timetuple()))
    
    print(str(pukul), str(tanggal),)
    
    # Membership
    if(menuPintuMasuk["Kartu Member"]):
        membership = "Y"
    else:
        membership = "N"
        
    barcodePintu = str(membership) + str(int(pukul) + int(tanggal)) + str(tipeKendaraan) + str(platNomor)
    print(barcodePintu)
    input("Press Enter to continue...")
    cls(0)
    

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