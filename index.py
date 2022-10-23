# Import Modules
import datetime as dt
from datetime import date, timedelta
import datetime
import time
from barcode import EAN13
from barcode.writer import ImageWriter
import os
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def pintuMasuk():
    if request.method == "POST":
       platNomor = request.form.get("tipeKendaraan")
       return platNomor
       
       return "Your name is "+first_name + last_name
    return render_template("form.html")
 
if __name__=='__main__':
   app.run()