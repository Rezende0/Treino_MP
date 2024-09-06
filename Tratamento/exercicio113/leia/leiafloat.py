def leiaFloat(msg):
    while True:
        try:
            n=float(input(msg))
        except (ValueError, TypeError):
            print('\33[31mERRO! Digite um número real válido.\33[m')
            continue
        except KeyboardInterrupt:
            print('\n\33[31mPrograma interrompido!\33[m')
            return 0
        else:
            return n