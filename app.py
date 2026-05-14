from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar as seleções
selecoes = []

@app.route('/')
def index():
    # Aqui dizemos ao Flask para usar o seu arquivo 'base.html'
    return render_template('base.html', selecoes=selecoes)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    selecao = request.form.get('selecao')
    regiao = request.form.get('regiao')
    copas = request.form.get('copas')
    
    if selecao:
        selecoes.append({
            'selecao': selecao,
            'regiao': regiao,
            'copas': copas
        })
    return redirect(url_for('index'))

@app.route('/ordenar/<tipo>')
def ordenar(tipo):
    global selecoes
    if tipo == 'alfa':
        selecoes.sort(key=lambda x: x['selecao'])
    elif tipo == 'reversa':
        selecoes.sort(key=lambda x: x['selecao'], reverse=True)
    return redirect(url_for('index'))

@app.route('/limpar')
def limpar():
    selecoes.clear()
    return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
    if 0 <= id < len(selecoes):
        selecoes.pop(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)