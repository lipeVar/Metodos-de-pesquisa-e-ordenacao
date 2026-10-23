import random
from flask import Blueprint, render_template, request
from Model.ordenador import Ordenador


main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    resultados = None
    
    if request.method == 'POST':
        tipo_entrada = request.form.get('tipo_entrada')
        algoritmo = request.form.get('algoritmo', '')
        numeros = []
        origem_dados = ""

        # Tratamento da entrada de dados
        if tipo_entrada == 'arquivo':
            arquivo = request.files.get('arquivo')
            
            if arquivo and arquivo.filename and arquivo.filename.endswith('.txt'):
                conteudo = arquivo.read().decode("utf-8")
                numeros = [int(linha.strip()) for linha in conteudo.splitlines() if linha.strip().isdigit()]
                origem_dados = f"Arquivo enviado ({len(numeros)} elementos)"
        
        elif tipo_entrada == 'gerador':
            tamanho = int(request.form.get('tamanho_gerador', 100))
            numeros = [random.randint(1, 100000) for _ in range(tamanho)]
            origem_dados = f"Lista gerada aleatoriamente ({tamanho} elementos)"

        # Processamento através do Model
        if numeros:
            model = Ordenador()
            
            # Utilizando sintaxe moderna do Python (3.10+)
            match algoritmo:
                case 'bolha':
                    res_model = model.bolha(numeros)
                case 'selecao':
                    res_model = model.selecao(numeros)
                case 'insercao':
                    res_model = model.insercao(numeros)
                case 'merge':
                    res_model = model.merge(numeros)
                case _:
                    res_model = None

            # Preparação dos dados para a View
            if res_model:
                resultados = {
                    'origem': origem_dados,
                    'algoritmo_nome': algoritmo.capitalize() + " Sort",
                    'tempo': f"{res_model.tempo_execucao:.6f}",
                    'trocas': res_model.total_trocas,
                    'comparacoes': res_model.total_comparacoes,
                    'previa': res_model.lista_ordenada[:15]
                }
                
    return render_template('index.html', resultados=resultados)