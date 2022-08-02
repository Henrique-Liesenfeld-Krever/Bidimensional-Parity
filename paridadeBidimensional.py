import numpy as np
import random


import math

###FUNÇÕES AUXILIARES

def insere_paridade(matriz,rows,columns,paridade_linhas,paridade_colunas):
    contador=0
    for i in range(rows):
        for j in range(columns):
            if matriz[i][j]==1:
                contador+=1
        if contador%2==1:
            contador=0
            matriz[i][columns]=1
            paridade_linhas+=1
    
    contador=0
    for i in range(columns):
        for j in range(rows):
            if matriz[j][i]==1:
                contador+=1
        if contador%2==1:
            contador=0
            matriz[rows][i]=1
            paridade_colunas+=1
            
    return(paridade_linhas,paridade_colunas)







### MAIN ###

rows = 4
columns = 4

matriz = np.zeros((rows+1,columns+1))

for i in range(rows):
    for j in range(columns):
        matriz[i][j] = random.randint(0, 1)
        
        

paridade_colunas=0
paridade_linhas=0

tupla = insere_paridade(matriz,rows,columns,paridade_linhas,paridade_colunas)

paridade_linhas=tupla[0]
paridade_colunas=tupla[1]

if paridade_colunas%2==1 & paridade_linhas%2==1:
    matriz[rows][columns]=1
    
print("matriz enviada\n",matriz)


linha_erro = random.randint(0, rows-1)
coluna_erro = random.randint(0, columns-1)

matriz[linha_erro][coluna_erro] = not matriz[linha_erro][coluna_erro]

print("matriz com erro\n","linha ",linha_erro,"coluna ",coluna_erro,"\n",matriz)
    
contador=0
contador_erros_linhas=0
linha_erro=0
for i in range(rows):
    for j in range(columns):
        if matriz[i][j]==1:
            contador+=1
    
    if (contador%2==0) and (matriz[i][columns]==1):
        print("erro linha ",i)
        contador_erros_linhas+=1
        linha_erro=i
    if (contador%2==1) and (matriz[i][columns]==0):
        print("erro linha ",i)
        contador_erros_linhas+=1
        linha_erro=i
    contador=0
        


        
contador=0
contador_erros_colunas=0
coluna_erro=0
for i in range(columns):
    for j in range(rows):
        if matriz[j][i]==1:
            contador+=1
    if (contador%2==0) & (matriz[rows][i]==1):
        print("erro coluna ",i)
        contador_erros_colunas+=1
        coluna_erro=i
    elif (contador%2==1) & (matriz[rows][i]==0):
        print("erro coluna ",i)
        contador_erros_colunas+=1
        coluna_erro=i

    contador=0
        
if contador_erros_colunas==1 & contador_erros_linhas==1:
    matriz[linha_erro][coluna_erro]= not matriz[linha_erro][coluna_erro]
    print("matriz corrigida\n", matriz)
else:
    print("impossivel corrigir")
    
        
    
        
#print(matriz)
        
    