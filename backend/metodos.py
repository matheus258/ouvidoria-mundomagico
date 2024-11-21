from operacoesBD import *


def listarManifestacao (conexao):
    print("criar metodo")
def adicionarManifestacao (conexao):
    print("criar metodo")
def alterarManifestacao(conexao):
    print("criar metodo")
def pesquisarManifestacao(conexao):
    print("criar metodo")
def quantidadeManifestacoes (conexao):
    manifestacao = listarBancoDados(conexao, 'select count(*) from Manifestacoes')
    if len(manifestacao) > 0:
        print('Temos',manifestacao[0][0], 'manifestações.')
    else:
        print('Não existem manifestações a serem exibidas')
