def entrada():
    dic = {'val':[], 'freq':[], 'freqAcu':[]}
    i = 1

    while True:
        entrada = float(input(f'\nDigite o {i}° valor: '))
        vezes = (float(input('Quantas vezes esse valores se repete?: ')))
        organizar(dic, entrada, vezes)  
               
        i += 1
        
        op = input('Deseja adicionar mais valores? [S/N]: ')[0].upper()
        if op == 'N':
            break
    Fi(dic)
    return dic

def organizar(dicOrg, entrada, vezes):
    n = 0

    n += vezes
    if len(dicOrg['val']) == 0:
            dicOrg['val'].append(entrada)
            dicOrg['freq'].append(vezes)
    else:
        for j in range(len(dicOrg['val'])):
            if dicOrg['val'][j] > entrada:
                dicOrg['val'].insert(j, entrada)
                dicOrg['freq'].insert(j, vezes)
                break
            elif entrada > dicOrg['val'][len(dicOrg['val'])-1]:
                dicOrg['val'].append(entrada)
                dicOrg['freq'].append(vezes)
                break
            elif j == len(dicOrg['val'])-1: 
                print('Valor já existente. Digite outro valor')
                break
    return dicOrg

def Fi(dicFi):
    j = 0
    n = 0
    for j in range(len(dicFi['val'])):
        n += dicFi['freq'][j]
        dicFi['freqAcu'].append(n)
    
