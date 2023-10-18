# NICKOLAS DE SOUZA SILVEIRA CORRÊA - RA: 185823
# VICTOR RICO MOURA SANTOS - RA: 191068

import sys
from io import StringIO


def ativacao(x1, x2, x0, w1, w2, w0):
    saidaIntermediaria = (x0*w0) + (x1*w1) + (x2*w2)
    saida = -1.0
    if (saidaIntermediaria > 0.0):
        saida = 1.0   
    return saidaIntermediaria, saida

def treinarAdaline(taxaAprendizado, x, w, target, nrMaxTreinos):
    buffer = StringIO()
    sys.stdout = buffer

    nrAcertos = 0
    nrTreinamentos = 0
    erro = 0
    NRCASOS = len(target)
    #print("taxaAprendizado: " + taxaAprendizado)       #DEBUG
    #print("X: " + str(x))
    #print("W: " + str(w))
    #print("target: " + str(target))
    #print("nrMaxTreinos: " + str(nrMaxTreinos))

    while (nrAcertos < NRCASOS and nrTreinamentos <= nrMaxTreinos):
        nrTreinamentos += 1
        nrAcertos = 0

        contador = 0
        for contador in range(NRCASOS):
            
            saidaIntermediaria, saida = ativacao(x[1][contador], x[2][contador], x[0], w[1], w[2], w[0])
            if (saida == target[contador]):
                nrAcertos += 1

            print("Treino: " + str(nrTreinamentos) + ", acertos: " + str(nrAcertos), file=buffer)
            
            if (nrAcertos == NRCASOS):  # convergiu
                break
            else:
                erro = target[contador] - saidaIntermediaria
                xQuadrado = (x[0]**2 + x[1][contador]**2 + x[2][contador]**2)

                w[0] += taxaAprendizado * erro * x[0] / xQuadrado
                w[1] += taxaAprendizado * erro * x[1][contador] / xQuadrado
                w[2] += taxaAprendizado * erro * x[2][contador] / xQuadrado

    if(nrAcertos == NRCASOS):
        print("\nCONVERGIU!", file=buffer)
    else:
        print("\nNÃO CONVERGIU!", file=buffer)
    print("Pesos Finais: w1: " + str(w[1]) + ", w2: " + str(w[2]) + "\n", file=buffer)

    sys.stdout = sys.__stdout__

    # Obter o conteúdo do buffer como uma string
    resultado = buffer.getvalue()
    buffer.close()  # Fechar o buffer

    return resultado

'''NRCASOS = 16  # mistureba do Nichollas
taxaAprendizado = 0.01  # constante de aprendizado (0 < taxaAprendizado < 2)
x = [1, [25, 22, 30, 27, 35, 38, 26, 33, 4, 6, 10, 3, 4, 15, 10, 7], [34, 37, 33, 37, 34, 39, 35, 37, 40, 38, 44, 42, 46, 45, 38, 48]]
w = [0, 4, -12]
target = [-1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1]  #target'''

'''taxaAprendizado = 0.0001  # constante de aprendizado (0 < taxaAprendizado < 2)
x = [1, [25, 22, 30, 27, 4, 6, 10, 3], [34, 37, 33, 37, 40, 38, 44, 42]]
w = [0, 0.02, 0.01]
target = [-1, -1, -1, -1, 1, 1, 1, 1]  #target
nrMaxTreinos = 5000
w = list(map(float, w))'''

#teste = treinarAdaline(taxaAprendizado, x, w, target, nrMaxTreinos)

'''NRCASOS = 1  # documento do Nichollas
taxaAprendizado = 0.01  # constante de aprendizado (0 < taxaAprendizado < 2)
x = [1, [2], [31]]
w = [0, 4, -12]
target = [1]  #target'''