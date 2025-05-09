from app import create_app

# Crea la instancia de la aplicación Flask para el Gestor de Biblioteca
app = create_app()

# Punto de entrada de la aplicación
if __name__ == '__main__':
    # Ejecuta el servidor Flask en modo desarrollo
    # host='0.0.0.0' permite el acceso desde otras máquinas en la red local
    # En producción, usar Gunicorn o un servidor WSGI similar y desactivar debug
    app.run(debug=True, host='0.0.0.0', port=5000)
