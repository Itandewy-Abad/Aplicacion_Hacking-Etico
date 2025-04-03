from flask import Flask, request, jsonify, render_template
import nmap

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Carga el HTML principal

@app.route('/escanear', methods=['POST'])
def escanear():
    data = request.json
    ip = data.get('ip')
    puertos = data.get('puertos', '1-1024')

    if not ip:
        return jsonify({"error": "Falta la dirección IP"}), 400

    escaner = nmap.PortScanner()
    escaner.scan(ip, puertos, arguments='-T4 -Pn')

    if ip not in escaner.all_hosts():
        return jsonify({"error": "No se encontró la IP o no respondió"}), 404

    resultados = {puerto: info['state'] for puerto, info in escaner[ip].get('tcp', {}).items()}
    return jsonify({"puertos_abiertos": resultados})

if __name__ == '__main__':
    app.run(debug=True)
