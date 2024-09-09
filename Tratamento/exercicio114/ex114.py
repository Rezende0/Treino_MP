import urllib
import urllib.request
import Tratamento.exercicio115.cor as cor

try:
    site=urllib.request.urlopen('https://www.youtube.com/watch?v=8jAykqxIeqw&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=50')
except:
    cor.red('Deu erro!')
else:
    print('Tudo em ordem.')