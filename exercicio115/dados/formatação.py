from cores import cor


def cabeçalho(txt):
    cor.lin()
    cor.cyan(txt.upper().center(40))
    cor.lin()


def menu(lista):
    cabeçalho('MENU PRINCPAL')
    for k,item in enumerate(lista):
        print(f'{cor.yellow(k+1)} - {cor.green(item)}')
    cor.lin()


def opção(valor):
    while True:
        try:
            opc=int(input(cor.yellow(valor)))
            if opc in (1,2,3,4):
                return opc
            else:
                cor.red('Erro! Digite uma das opções disponíveis no menu')
        except ValueError:
            cor.red('Erro! Digite uma das opções disponíveis no menu')
        except KeyboardInterrupt:
            opc=4
            return opc
        
        
def leiaInt(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError, TypeError):
            print('\33[31mERRO! Digite um número inteiro válido.\33[m')
            continue
        except KeyboardInterrupt:
            print('\n\33[31mPrograma interrompido!\33[m')
            return 0
        else:
            return n