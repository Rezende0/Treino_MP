def leiadinheiro(msg):
    while True:
        p=input(msg).strip().replace(',','.')
        if p.isalpha():
            print('\033[0;31mErro! Valor inválido.\33[m')
        else:
            return float(p)