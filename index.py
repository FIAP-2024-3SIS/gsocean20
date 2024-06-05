from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():

    region = request.form['region']
    species = request.form['species']
    conservation_status = request.form['conservation_status']
    water_temperature = request.form['water_temperature']
    ph = request.form['ph']
    pollution_leves = request.form['pollution_leves']
    
    api_url = {f'https://fiap-3sis-gs-20241.azurewebsites.net/OceanData?regiao={region}&especie={species}&statusConservacao={conservation_status}&temperaturaMin={water_temperature}&temperaturaMax={water_temperature}&phMin={ph}&phMax={ph}&nivelPoluicao={pollution_leves}'}
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
        return "Sucesso"
    else:
        return "Erro ao acessar a API"

if __name__ == '__main__':
    app.run(debug=True)
