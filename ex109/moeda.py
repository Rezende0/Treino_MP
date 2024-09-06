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