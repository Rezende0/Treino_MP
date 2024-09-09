from dados import formatação,resultado
from dados import arquivo
from time import sleep

arq='Cadastro'
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)
while True:
    formatação.menu(('Ver Pessoas Cadastradas','Cadastrar Novas Pessoas','Retirar uma pessoa do cadastro','Sair do Sistema'))
    opc=formatação.opção('Deseja qual opção? ')
    resultado.opcao(opc,arq)
    if opc==4:
        break
    print()
    sleep(0.7)