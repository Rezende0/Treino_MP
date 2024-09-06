def leiadinheiro(msg):
    while True:
        try:
            p=float(input(msg).replace(',','.'))
            
        except (ValueError,TypeError):
            print('\33[31mErro! Valor inválido, tente novamente.\33[m')
            continue
        except KeyboardInterrupt:
            print('\33[31m\nPrograma Interrompido!\33[m')
            return 0
        else:
            return p