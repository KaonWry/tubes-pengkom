# Import Modules
import datetime as dt
from datetime import date, timedelta
import datetime
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
    return render_template("masuk.html")
    # if request.method == "POST":
    #    platNomor = request.form.get("tipeKendaraan")
    #    return platNomor
 
if __name__=='__main__':
    app.run(debug=True)