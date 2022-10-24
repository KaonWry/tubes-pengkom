# Import Modules
from crypt import methods
import datetime as dt
from datetime import date, timedelta
import datetime
import re
import sys
import time
import treepoem
import os
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)  


# Program startup
@app.route("/")
def startup():
    return render_template("tentang-kami.html")


# Program pintu masuk
@app.route("/m", methods =["POST", "GET"])
def pintuMasuk():
    if (request.method == "POST"):
        tipeKendaraan = request.form.get("tipeKendaraan")
        if (tipeKendaraan == "Motor"):
            tipeKendaraan = "MT"
        elif (tipeKendaraan == "Mobil"):
            tipeKendaraan = "MB"
        elif (tipeKendaraan == "Truk/bus"):
            tipeKendaraan = "TR"
        platNomor = ((request.form.get("platNomor")).replace(" ", "")).upper()
        membership = request.form.get("membership")
        waktu = request.form.get("waktuMasuk")
        waktu = waktu.split(" ")
        # Tanggal to seconds
        tanggal = waktu[0]
        tanggal = int(time.mktime(datetime.datetime.strptime(tanggal, "%m/%d/%Y").timetuple()))
        # Pukul to seconds
        pukul = waktu[1]
        pukul = list(map(int, pukul.split(":")))
        if (waktu[2] == "PM"):
            pukul[0] += 12
        pukul = ((int(pukul[0])*60)+int(pukul[1]))*60
        # print (tipeKendaraan, file=sys.stderr)
        # print (platNomor, file=sys.stderr)
        # print (membership, file=sys.stderr)
        # print (isiBarcode, file=sys.stderr)
        isiBarcode = f"{tipeKendaraan}-{platNomor}-{pukul + tanggal}-{membership}"
        gambarBarcode = treepoem.generate_barcode(
        barcode_type="code128",  # One of the BWIPP supported codes.
        data = isiBarcode,
        )
        gambarBarcode.convert("1").save("static/img/output.png")
        return render_template("masuk.html", barcodeIsi = isiBarcode, barcode = gambarBarcode)
    else:
        return render_template("masuk.html")
    
    
    
# Program pintu keluar
@app.route("/k", methods=["POST", "GET"])
def pintuKeluar():
    if (request.method == "POST"):
        barcode = request.form.get("barcode").split("-")
        tipeKendaraan = barcode[0]
        platNomor = barcode[1]
        waktuTiba = int(barcode[2])
        membership = barcode[3]
        waktu = request.form.get("waktuKeluar")
        waktu = waktu.split(" ")
        # Tanggal to seconds
        tanggal = waktu[0]
        tanggal = int(time.mktime(datetime.datetime.strptime(tanggal, "%m/%d/%Y").timetuple()))
        # Pukul to seconds
        pukul = waktu[1]
        pukul = list(map(int, pukul.split(":")))
        if (waktu[2] == "PM"):
            pukul[0] += 12
        pukul = ((int(pukul[0])*60)+int(pukul[1]))*60
        jmlhBayar = int(request.form.get("jmlhBayar"))   
        
        # Biaya jam pertama 3000(motor), 5000(mobil), 8000(truk/bus)
        # Biaya setiap jam 2000(motor), 3000(mobil), 5000(truk/bus)
        # Member gratis biaya jam pertama
        
        # Hitung lama parkir
        waktuParkir = ((pukul + tanggal) - waktuTiba)/3600
        
        # Hitung biaya jam pertama
        if(((pukul + tanggal) - waktuTiba < 5*60) or (membership == "Y")):
            biayaJam1 = 0
        else:
            if (tipeKendaraan == "MT"):
                biayaJam1 = 3000
            elif (tipeKendaraan == "MB"):
                biayaJam1 = 5000
            elif (tipeKendaraan == "TR"):
                biayaJam1 = 8000
                
        # Pembulatan keatas waktu parkir
        if (waktuParkir == int(waktuParkir)):
            waktuParkir = int(waktuParkir)
        else:
            waktuParkir = int(waktuParkir) + 1
        
        # Hitung biaya parkir
            
        if (tipeKendaraan == "MT"):
            biayaParkir = biayaJam1 + ((waktuParkir-1) * 2000)
        elif (tipeKendaraan == "MB"):
            biayaParkir = biayaJam1 + ((waktuParkir-1) * 3000)
        elif (tipeKendaraan == "TR"):
            biayaParkir = biayaJam1 + ((waktuParkir-1) * 5000)
            
        kembalian = jmlhBayar - biayaParkir
        # print (biayaParkir, kembalian, file=sys.stderr)
        
        # List output
        platNomor = re.split('(\d+)', platNomor)
        space = " "
        if (tipeKendaraan == "MT"):
            tipeKendaraan = "Motor"
        elif (tipeKendaraan == "MB"):
            tipeKendaraan = "Mobil"
        elif (tipeKendaraan == "TR"):
            tipeKendaraan = "Truk/bus"

        kendaraan = f"{tipeKendaraan}, {space.join(platNomor)}"
        
        masuk = datetime.datetime.fromtimestamp(waktuTiba).strftime('%d-%m-%Y %H:%M')
        keluar = datetime.datetime.fromtimestamp(pukul + tanggal).strftime('%d-%m-%Y %H:%M')
        lamaParkir = (pukul + tanggal) - waktuTiba
        lamaParkir = f"{int(lamaParkir/3600)}:{int((lamaParkir%3600)/60)}"
        
        if (membership == "Y"):
            membership = "Ada"
        elif (membership == "N"):
            membership = "Tidak ada"
        
        biayaParkir = f"Rp.{biayaParkir:,},00"
        pembayaran = f"Rp.{jmlhBayar:,},00"
        kembalian = f"Rp.{kembalian:,},00"
        
        return render_template("keluar.html", kendaraan=kendaraan, masuk=masuk, keluar=keluar, lamaParkir=lamaParkir, membership=membership, biayaParkir=biayaParkir, pembayaran=pembayaran, kembalian=kembalian)

    else:
        return render_template("keluar.html")
    
    
    
    
# Program buka pintu masuk
@app.route("/bukaPintuMasuk")
def bukaPintuMasuk():
    return render_template("masuk.html")


# Program buka pintu keluar
@app.route("/bukaPintuKeluar")
def bukaPintuKeluar():
    return render_template("keluar.html")

# Program buka rincian harga
@app.route("/bukaTentangKami")
def bukaTentangKami():
    return render_template("tentang-kami.html")


if __name__=='__main__':
    app.run(debug=True)