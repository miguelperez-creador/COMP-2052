
from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

@app.route('/info', methods=['GET'])
def info():
    
    info_sistema = {
        "nombre_sistema": "Gestión de Usuarios",
        "version": "1.0",
        "descripcion": "Sistema para gestionar usuarios."
    }
    return jsonify(info_sistema)


@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
  
    data = request.get_json()

   
    if not data or 'nombre' not in data or 'correo' not in data:
        return jsonify({"error": "Faltan campos necesarios: nombre o correo."}), 400

    nombre = data['nombre']
    correo = data['correo']
    
    usuario = {"nombre": nombre, "correo": correo}
    usuarios.append(usuario)
    
    
    return jsonify({"mensaje": "Usuario creado con éxito", "usuario": usuario}), 201

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
 
    return jsonify(usuarios)


if __name__ == '__main__':
    app.run(debug=True)















