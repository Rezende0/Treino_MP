from dados.formatação import cabeçalho,leiaInt
from dados import arquivo
from cores import cor
def opcao(n,a):
    if n==1:
        cabeçalho('pessoas cadastradas')
        arquivo.lerArquivo(a)
    elif n==2:
        try:
            cabeçalho('novo cadastro')
            nome=input(cor.yellow('Nome: ')).strip().capitalize()
            idade=leiaInt(cor.yellow('Idade: '))
            arquivo.cadastrar(a,nome,idade)
        except:
            cor.red('\nErro! Cadastro não realizado.')
    elif n==3:
        cabeçalho('removendo')
    else:
        cor.magenta('Obrigado pela prefência de programa!')
        cor.magenta('Volte sempre e bom trabalho!')