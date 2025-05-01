from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "aplicacion": "Gestion de Productos y Usuarios",
        "version": "1.0",
        "autor": "nombre_sistema"
    })

@app.route('/mensaje', methods=['POST'])
def mensaje():
    
    data = request.get_json()

    
    if not data or 'nombre' not in data:
        return jsonify({"error": "Falta el campo 'nombre' en el JSON"}), 400

    
    nombre = data['nombre']
    return jsonify({
        "respuesta": f"Hola, {nombre}. Tu mensaje ha sido recibido correctamente"
    })

if __name__ == '__main__':
    
    app.run(debug=True)
