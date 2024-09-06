def moeda(preço,cotação='R$'):
    return  f'{cotação}{preço:.2f}'.replace('.',',')

def metade(preço):
    return preço/2


def dobro(preço):
    return preço*2


def aumentar(preço,porcentagem):
    return preço*(porcentagem/100)+preço


def diminuir(preço,porcentagem):
    return preço-preço*(porcentagem/100)