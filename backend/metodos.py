from operacoesBD import *


def listarManifestacao (conexao):
    manifestacao = listarBancoDados(conexao, 'select * from Manifestacoes')
    if len(manifestacao) > 0:
        print('Listar de manifestações')
        for item in manifestacao:
            print('Manifestação: ', item[0], '\nNome: ', item[1], '\nDescrição: ', item[2], '\nTipo: ', item[3])
    else:
        print('Não existem manifestações a serem exibidas')
        
def adicionarManifestacao (conexao):
    consultaInserir = 'insert into Manifestacoes(descricao, autor, categoria) values(%s,%s,%s)'

    descricao = input('Digite a sua manifestacao: ')
    autor = input('Digite o seu nome: ')
    categoria = input('Digite o tipo de manifestacao: ')
    valores = [descricao, autor, categoria]
    
    insertNoBancoDados(conexao, consultaInserir, valores)
    
def alterarManifestacao(conexao):
    codigoAlterar = input("Digite o código da manifestação que deseja alterar: ")
    novaDescricao = input("Digite a nova descrição para a manifestação: ")
    consultaAlterar = "update Manifestacoes set descricao = %s where codigo = %s"
    valores = [novaDescricao, codigoAlterar]
    atualizarBancoDados(conexao, consultaAlterar, valores)
    print("- Manifestação alterada com sucesso!")

def pesquisarManifestacao(conexao):
    print("escolha o modo que você quer pesquisar!")
    print("1) pesquisar por codigo")
    print("2) pesquisar por categoria")
    modo = int(input("digite a opção."))
    if modo == 1:
        codigo = int(input("digite o codigo da manifestação que você deseja pesquisar: "))
        consulta = f"select * from manifestacoes where codigo = '{codigo}'"
        resultados = listarBancoDados(conexao, consulta)

    elif modo == 2:
        categoria = input("digite o numero da categoria que você deseja pesquisar. ")
        consulta = f"select * from manifestacoes where categoria like '%{categoria}%'"
        resultados = listarBancoDados(conexao, consulta)
        
    if resultados:
        for item in resultados:
            print("Código: " + str(item[0]) + ", Descrição: " + item[1] + ", Autor: " + item[2] + ", Categoria: " + item[3])

    else:
        print('Temos',manifestacao[0][0], 'manifestações.')

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

    if linhasAfetadas:
        print("Manifestação Removida com sucesso !")
    else :
        print("Não existe Manifestação para o codigo informado.")
        
