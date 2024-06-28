from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def beranda():
    return render_template('beranda.html')

@app.route("/transaksi")
def transaksi():
    return render_template('transaksi.html')

@app.route("/produk")
def produk():
    return render_template('produk.html')

@app.route("/laporan")
def laporan():
    return render_template('laporan.html')

@app.route("/pengaturan")
def pengaturan():
    return render_template('pengaturan.html')