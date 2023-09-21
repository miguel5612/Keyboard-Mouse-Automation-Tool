from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Esto es necesario para utilizar 'session' en Flask

API_URL = "http://localhost:5000"

@app.route('/')
def index():
    fields = session.get('fields', [])
    return render_template('index.html', fields=fields)

@app.route('/define_structure', methods=['POST'])
def define_structure():
    fields = request.form.getlist('fields')
    session['fields'] = fields
    structure = {field: 'string' for field in fields}  # Por simplicidad, todos los campos se definen como string
    response = requests.post(API_URL + "/define_structure", json=structure)
    return redirect(url_for('index'))

@app.route('/add_record', methods=['POST'])
def add_record():
    record = request.form.to_dict()
    response = requests.post(API_URL + "/add_record", json=record)
    return redirect(url_for('index'))

@app.route('/query', methods=['GET'])
def query():
    field = request.args.get('field')
    value = request.args.get('value')
    response = requests.get(API_URL + f"/query?field={field}&value={value}")
    return render_template('query_results.html', results=response.json(), fields=session.get('fields', []))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
