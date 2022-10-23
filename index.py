# Import Modules
import datetime as dt
from datetime import date, timedelta
import datetime
import sys
import time
import treepoem
import os
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)  

# Program pintu masuk
@app.route('/', methods =["GET", "POST"])
def pintuMasuk():
    if (request.method == "POST"):
        tipeKendaraan = request.form.get("tipeKendaraan")
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
        isiBarcode = str(membership) + str(pukul + tanggal) + str(tipeKendaraan) + str(platNomor)
        gambarBarcode = treepoem.generate_barcode(
        barcode_type="code128",  # One of the BWIPP supported codes.
        data = isiBarcode,
        )
        gambarBarcode.convert("1").save("static/img/output.png")
        return render_template("masuk.html", barcodeIsi = isiBarcode, barcode = gambarBarcode)
    else:
        return render_template("masuk.html")


# Program pintu 

if __name__=='__main__':
    app.run(debug=True)