from flask import Flask, request, jsonify

app = Flask(__name__)

# Estructura básica para almacenar datos
data_structure = {}
data = []

@app.route('/define_structure', methods=['POST'])
def define_structure():
    global data_structure
    data_structure = request.json
    return "Structure defined!"

@app.route('/add_record', methods=['POST'])
def add_record():
    record = request.json
    data.append(record)
    return "Record added!"

@app.route('/query', methods=['GET'])
def query():
    field = request.args.get('field')
    value = request.args.get('value')
    results = [record for record in data if record.get(field) == value]
    return jsonify(results)

@app.route('/data', methods=['GET'])
def get_data():
    format_type = request.args.get('format', 'json').lower()
    
    if format_type == 'json':
        return jsonify(data)
    # Puedes agregar más lógica aquí para otros formatos...
    # Por ejemplo: if format_type == 'xml': ...
    
    return "Unsupported format", 400

if __name__ == '__main__':
    app.run(debug=True)
