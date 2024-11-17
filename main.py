import segno
from flask import Flask, render_template, request, send_file, url_for, redirect
from flask_bootstrap import Bootstrap5
import io
import base64


app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route("/qr", methods=[ 'POST','GET']) 
def QR_generator():
    
    qr_text =request.form["qrcreate"]
    qr=segno.make(qr_text)
    img = io.BytesIO()
    qr.save(img, kind='png', scale=10)
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode("utf-8") 
    return render_template('display.html', image=img_base64) 

if __name__=='__main__':
    app.run(debug=True)
    