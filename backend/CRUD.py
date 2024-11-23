from flask import Flask, request, jsonify
from flask_cors import CORS
from operacoesBD import *

conexao = criarConexao('localhost', 'root', 'Kar21985@', 'ouvidoria_final')

app = Flask(__name__)
CORS(app)
# Endpoint para listar todas as manifestações (GET)
@app.route('/manifestacoes', methods=['GET'])
def listar_manifestacoes():
    manifestacoes = listarBancoDados(conexao, 'SELECT * FROM Manifestacoes')
    if manifestacoes:
        # Mapeando os campos na ordem correta
        return jsonify([
            {
                'codigo': item[0],
                'autor': item[1],  # Agora correto: autor é o segundo campo
                'descricao': item[2],  # Agora correto: descricao é o terceiro campo
                'categoria': item[3]
            }
            for item in manifestacoes
        ])
    return jsonify({'mensagem': 'Não existem manifestações a serem exibidas'}), 404

# Endpoint para adicionar uma manifestação (POST)
@app.route('/manifestacoes', methods=['POST'])
def adicionar_manifestacao():
    dados = request.get_json()
    # Validar os dados recebidos
    descricao = dados.get('descricao')
    autor = dados.get('autor')
    categoria = dados.get('categoria')

    if not descricao or not autor or not categoria:
        return jsonify({'mensagem': 'Todos os campos (descricao, autor, categoria) são obrigatórios!'}), 400

    # Corrigir a ordem dos campos para bater com a tabela
    consulta_inserir = 'INSERT INTO Manifestacoes (autor, descricao, categoria) VALUES (%s, %s, %s)'
    valores = (autor, descricao, categoria)
    insertNoBancoDados(conexao, consulta_inserir, valores)

    return jsonify({'mensagem': 'Manifestação adicionada com sucesso!'}), 201
# Endpoint para alterar uma manifestação (PUT)
@app.route('/manifestacoes/<int:codigo>', methods=['PUT'])
def alterar_manifestacao(codigo):
    dados = request.get_json()
    descricao = dados.get('descricao')
    autor = dados.get('autor')
    categoria = dados.get('categoria')

    if not descricao or not autor or not categoria:
        return jsonify({'mensagem': 'Todos os campos (descricao, autor, categoria) são obrigatórios para atualizar!'}), 400

    consulta_alterar = '''
        UPDATE Manifestacoes
        SET descricao = %s, autor = %s, categoria = %s
        WHERE codigo = %s
    '''
    valores = (descricao, autor, categoria, codigo)
    linhas_afetadas = atualizarBancoDados(conexao, consulta_alterar, valores)

    if linhas_afetadas > 0:
        return jsonify({'mensagem': 'Manifestação alterada com sucesso!'})
    return jsonify({'mensagem': 'Manifestação não encontrada!'}), 404

# Endpoint para excluir uma manifestação (DELETE)
@app.route('/manifestacoes/<int:codigo>', methods=['DELETE'])
def excluir_manifestacao(codigo):
    consulta_excluir = "DELETE FROM Manifestacoes WHERE codigo = %s"
    linhas_afetadas = excluirBancoDados(conexao, consulta_excluir, (codigo,))

    if linhas_afetadas > 0:
        return jsonify({'mensagem': f'Manifestação com o código {codigo} excluída com sucesso!'})
    return jsonify({'mensagem': 'Manifestação não encontrada!'}), 404

# Endpoint para pesquisar manifestações por código ou categoria (GET com parâmetros)
@app.route('/manifestacoes/pesquisar', methods=['GET'])
def pesquisar_manifestacao():
    codigo = request.args.get('codigo')
    categoria = request.args.get('categoria')

    if codigo:
        consulta = 'SELECT * FROM Manifestacoes WHERE codigo = %s'
        resultados = listarBancoDados(conexao, consulta, (codigo,))
    elif categoria:
        consulta = "SELECT * FROM Manifestacoes WHERE categoria LIKE %s"
        resultados = listarBancoDados(conexao, consulta, ('%' + categoria + '%',))
    else:
        return jsonify({'mensagem': 'Informe um código ou categoria para pesquisar!'}), 400

    if resultados:
        return jsonify([{'codigo': item[0], 'descricao': item[1], 'autor': item[2], 'categoria': item[3]} for item in resultados])
    return jsonify({'mensagem': 'Nenhuma manifestação encontrada.'}), 404

# Rodando o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
