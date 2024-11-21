from metodos import *

conexao = criarConexao('127.0.0.1','vinicius','','ouvidoria_final')
opcao = 1

while opcao != 7:
    print("\n1) Listar Manifestações\n2) Adicionar Manifestação \n3) Pesquisar Manifestação \n4) Remover Manifestação\n5) Alterar Manifestação\n6) Quantidade de Manifestações \n7)Sair")
    opcao = int(input('Digite a sua opção: '))

    if opcao == 1:
      listarManifestacao(conexao)
    elif opcao == 2:
        adicionarManifestacao(conexao)
    elif opcao == 3:
        pesquisarManifestacao(conexao)
    elif opcao == 4:
        print('Remover')
    elif opcao == 5:
       alterarManifestacao(conexao)
    elif opcao == 6:
        quantidadeManifestacoes(conexao)
    elif opcao !=7:
        print('Sair')
    print('Obrigado por usar a Ouvidoria!')

encerrarConexao(conexao)
