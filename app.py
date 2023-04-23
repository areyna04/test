from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/tasks', methods=['GET', 'POST'])
def tasks():
    return jsonify({'message': 'Esto Funciona'})

if __name__ == '__main__':
    app.run(debug=True)