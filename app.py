from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Server aktif!"})

@app.route('/process')
def process():
    # Simulasi proses berat
    time.sleep(0.5)
    return jsonify({"status": "Selesai memproses data"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
