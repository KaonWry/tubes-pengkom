# Import Modules
import datetime as dt
from datetime import date, timedelta
import datetime
import sys
import time
import barcode
from barcode.writer import ImageWriter
import os
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def pintuMasuk():
    tipeKendaraan = request.form.get("tipeKendaraan")
    print (tipeKendaraan, file=sys.stderr)
    platNomor = ((request.form.get("platNomor")).replace(" ", "")).upper()
    print (platNomor, file=sys.stderr)
    membership = request.form.get("membership")
    print (membership, file=sys.stderr)
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
    isiBarcode = str(membership) + str(pukul + tanggal) + str(tipeKendaraan) + platNomor
    print (isiBarcode, file=sys.stderr)
    return render_template("masuk.html", barcodeIsi = isiBarcode)
 
if __name__=='__main__':
    app.run(debug=True)