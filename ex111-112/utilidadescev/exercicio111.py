from moeda import moedas
from dados import dado

p=dado.leiadinheiro('Digite um preço: R$')
moedas.resumo(p,80,35)