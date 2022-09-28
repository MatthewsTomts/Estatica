from os import system
from Calculo import media, mediana, moda, ampTot, disp, cofVar
from Entrada import entrada
from time import sleep

system('clear')

dic = entrada()

media = media(dic)
mediana = mediana(dic)
moda = moda(dic)

ampTot = ampTot(dic)
disp = disp(dic)
cofVar = cofVar(dic)

print('Calculando...')
sleep(1)
system('clear')

print('Média:', media)
print('Mediana:', mediana)
print('Moda:', moda)

print('\nAmplitude Total:', ampTot)
print('Dispersão Padrão:', disp)
print('Coeficiente de Variação:', cofVar)

print('\nxi:', dic['val'])
print('fi:', dic['freq'])
print('Fi:', dic['freqAcu'])
