from math import floor

def media(dic):
    soma = 0
    for i in range(len(dic['val'])):
        soma += dic['val'][i] * dic['freq'][i]
    return soma / len(dic['val'])

def mediana(dic):
    n = dic['freqAcu'][len(dic['freqAcu'])-1] 
    mediana = 0

    if n % 2 == 0:
        for i in range(len(dic['val'])):
            if dic['freqAcu'][i] > floor(n / 2):
                mediana = dic['val'][i]
                break
            elif dic['freqAcu'][i] == floor(n / 2):
                mediana = (dic['val'][i] + dic['val'][i+1]) / 2
                break
    else:
        for i in range(len(dic['val'])):
            if dic['freqAcu'][i] >= floor(n / 2):
                mediana = dic['val'][i]
                break
    return mediana

def moda(dic):
    maior = 0
    moda = []
    for freq in dic['freq']:
        if maior < freq:
            maior = freq
    
    for i in range(len(dic['freq'])):
        if dic['freq'][i] == maior:
            moda.append(dic['val'][i])
    
    if len(moda) == len(dic['freq']):
        moda = 'Essa sequência não tem moda'
    return moda

def ampTot(dic):
    return dic['val'][len(dic['val']) - 1] - dic['val'][0] 


def disp(dic):
    return 'Sob construção'

def cofVar(dic):
    return 'Sob construção'