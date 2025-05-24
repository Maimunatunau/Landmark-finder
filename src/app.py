# src/app.py

from flask import Flask, request, render_template
import os
from predict import predict

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        path = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(path)
        label, prob = predict(path)
        return render_template('result.html', label=label, prob=prob, filename=f.filename)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
