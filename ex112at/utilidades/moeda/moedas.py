def moeda(preço,cotação='R$'):
    return  f'{cotação}{preço:.2f}'.replace('.',',')


def metade(preço,form=False):
    met=preço/2
    return met if form==False else moeda(met)


def dobro(preço,form=False):
    dob=preço*2
    return dob if form is False else moeda(dob)


def aumentar(preço,porcentagem,form=False):
    aum=preço*(porcentagem/100)+preço
    return aum if not form else moeda(aum)


def diminuir(preço,porcentagem,form=False):
    dim=preço-preço*(porcentagem/100)
    if form==True:
        return moeda(dim)
    return dim


def resumo(preço,aumento,redução):
    print('-'*33)
    print('RESUMO DO VALOR'.center(33))
    print('-'*33)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço,True)}')
    print(f'Metade do preço: \t{metade(preço,True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preço,aumento,True)}')
    print(f'{redução}% de redução: \t{diminuir(preço,redução,True)}')
    print('-'*33)
    