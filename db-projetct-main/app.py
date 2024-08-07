from flask import Flask, request, jsonify, render_template, send_file
from scripts.data_generator import generate_mailing
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_report', methods=['GET'])
def generate_report():
    carteira = request.args.get('carteira')
    
    if not carteira:
        return jsonify({"error": "Missing required parameters"}), 400
    
    result = generate_mailing(carteira)
    
    if "error" in result:
        return jsonify(result), 400
    
    return jsonify(result)

@app.route('/download_report', methods=['GET'])
def download_report():
    file_path = request.args.get('file_path')
    
    if not file_path or not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404
    
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists('reports'):
        os.makedirs('reports')
    app.run(debug=True)