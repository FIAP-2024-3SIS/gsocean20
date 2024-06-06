from flask import Flask, render_template, request
from json2html import json2html
from urllib.parse import urlencode
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def result():

    region = request.form.get('region', '')
    species = request.form.get('species', '')
    conservation_status = request.form.get('conservation-status', '')
    water_temperature = request.form.get('water_temperature', '')
    ph = request.form.get('ph', '')
    pollution_levels = request.form.get('pollution-leves', '')

    params = {}

    if region:
        params['regiao'] = region
    if species:
        params['especie'] = species
    if conservation_status:
        params['statusConservacao'] = conservation_status
    if water_temperature:
        params['temperaturaMin'] = params['temperaturaMax'] = water_temperature
    if ph:
        params['phMin'] = ph
        params['phMax'] = ph

    if pollution_levels:
        params['nivelPoluicao'] = pollution_levels

    api_url = 'https://fiap-3sis-gs-20241.azurewebsites.net/OceanData?' + urlencode(params).replace("+","%20")
 
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        html = "String Busca: <br>"+ api_url 
        html_table = json2html.convert(json = data)
        html_table = html + html_table

        return render_template('index.html', html_table="")
    else:
        return "Erro ao acessar a API"

if __name__ == '__main__':
    app.run(debug=True)
