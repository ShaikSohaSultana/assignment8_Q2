from flask import Flask, render_template, request, jsonify, send_from_directory
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Here you can include your model prediction logic
    email_text = request.json['email']
    # For demonstration, let's assume any text containing "spam" is classified as spam
    prediction = 'Spam' if 'spam' in email_text else 'Not Spam'
    return jsonify({'prediction': prediction})

@app.route('/static/<path:filename>')
def send_csv(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
