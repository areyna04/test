from flask import Flask, request, jsonify

app = Flask(__name__)




@app.route('/api/auth/login', methods=['POST'])
def upload_file():
    # Obtener el archivo enviado
    file = request.files['file']

    # Guardar el archivo en disco
    file.save(file.filename)

    # Retornar una respuesta JSON
    return jsonify({'message': 'Archivo recibido correctamente.'})

if __name__ == '__main__':
    app.run(debug=True)