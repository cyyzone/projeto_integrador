from flask import Flask, render_template, request

app = Flask(__name__)

# --- ESTRUTURA DE DADOS (Simulando um Banco de Dados) ---
# Cada questão é um dicionário dentro de uma lista.
questoes_treinamento = [
    {
        "id": 1,
        "pergunta": "Qual é o primeiro passo ao atender um cliente irritado?",
        "opcoes": ["Pedir calma", "Escutar ativamente", "Desligar o telefone"],
        "correta": "Escutar ativamente"
    },
    {
        "id": 2,
        "pergunta": "O sistema X funciona em modo offline?",
        "opcoes": ["Sim, totalmente", "Não", "Apenas para leitura"],
        "correta": "Sim, totalmente"
    },
    {
        "id": 3,
        "pergunta": "Onde consultar o protocolo de atendimento?",
        "opcoes": ["No Google", "Na Base de Conhecimento Interna", "Perguntar ao colega"],
        "correta": "Na Base de Conhecimento Interna"
    }
]

# --- ROTAS DO SISTEMA ---

@app.route('/')
def home():
    # Rota da página inicial que contém o material de estudo
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    # Rota que exibe o quiz
    return render_template('quiz.html', questoes=questoes_treinamento)

@app.route('/resultado', methods=['POST'])
def resultado():
    # --- LÓGICA DE PROGRAMAÇÃO E GAMIFICAÇÃO ---
    respostas_usuario = request.form
    pontos = 0
    total_questoes = len(questoes_treinamento)
    
    # Verifica cada resposta
    for questao in questoes_treinamento:
        # Pega a resposta enviada pelo usuário (o ID é usado como chave)
        resposta_escolhida = respostas_usuario.get(str(questao['id']))
        
        if resposta_escolhida == questao['correta']:
            pontos += 10 # Gamificação: 10 pontos por acerto (XP)

    # Lógica de Feedback (Gamificação)
    if pontos == total_questoes * 10:
        mensagem = "Parabéns! Você é um expert!"
        classe_css = "sucesso"
    elif pontos >= (total_questoes * 10) / 2:
        mensagem = "Bom trabalho, mas pode melhorar."
        classe_css = "aviso"
    else:
        mensagem = "Recomendamos refazer o treinamento."
        classe_css = "erro"

    return render_template('index.html', resultado=True, pontos=pontos, mensagem=mensagem, classe=classe_css)

if __name__ == '__main__':
    app.run(debug=True)