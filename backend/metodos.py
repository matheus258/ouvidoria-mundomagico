from operacoesBD import *


def listarManifestacao (conexao):
    print("criar metodo")
def adicionarManifestacao (conexao):
    consultaInserir = 'insert into Manifestacoes(descricao, autor, categoria) values(%s,%s,%s)'

    descricao = input('Digite a sua manifestacao: ')
    autor = input('Digite o seu nome: ')
    categoria = input('Digite o tipo de manifestacao: ')

    valores = [descricao, autor, categoria]

    insertNoBancoDados(conexao, consultaInserir, valores)
    
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
        
def removerPeloCodigo(conexao) :
    codigoRemover = int(input("Digite o codigo para remover:"))

    consultaRemover = " delete from Manifestacoes where codigo = %"
    linhasAfetadas = excluirBancoDados(conexao, consultaRemover, (codigoRemover,))

    if linhasAfetadas > 0:
        print("Manifestação Removida com sucesso !")
    else :
        print("Não existe Manifestação para o codigo informado.")
        
