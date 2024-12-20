from cores import cor
def arquivoExiste(nome):
    try:
        a=open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a=open(nome,'wt+')
        a.close()
    except:
        cor.red('Houve um erro na criação do arquivo!')
    else:
        print(cor.green(f'Arquivo {nome} criado com sucesso!'))


def lerArquivo(nome):
    try:
        a=open(nome,'rt')
    except:
        cor.red('Erro ao ler o arquivo!')
    else:
        for linha in a:
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a=open(arq,'at')
    except:
        cor.red('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            cor.red('Houve um erro na hora de escrever os dados!')
        else:
            print(cor.green(f'Novo Registo de {nome} adicionado.'))
            a.close()