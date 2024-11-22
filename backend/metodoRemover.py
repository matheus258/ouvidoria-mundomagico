from menu import conexao
from operacoesbd import excluirBancoDados


def removerPeloCodigo(conexao) :
    codigoRemover = int(input("Digite o codigo para remover:"))

    consultaRemover = " delete from Manifestacoes where codigo = %"
    valores = [codigoRemover]
    linhasAfetadas = excluirBancoDados(conexao, consultaRemover)

    if linhasAfetadas > 0:
        print("Manifestação Removida com sucesso !")
    else :
        print("Não existe Manifestação para o codigo informado.")