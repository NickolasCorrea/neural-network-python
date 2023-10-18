# NICKOLAS DE SOUZA SILVEIRA CORRÊA - RA: 185823
# VICTOR RICO MOURA SANTOS - RA: 191068

import sys
from io import StringIO

def ativacao(x1, x2, w1, w2):
    net = x1*w1 + x2*w2
    y = -1.0
    if (net >= 0.0):
        y = 1.0
    return y

def treinarPerceptron(taxaAprendizado, x, w, target, nrMaxTreinos):
    buffer = StringIO()
    sys.stdout = buffer

    nrTreinamentos = 0
    nrAcertos = 0
    erro1 = 0.0
    erro2 = 0.0
    NRCASOS = len(target)
    #print("taxaAprendizado: " + str(taxaAprendizado))       #DEBUG
    #print("X: " + str(x))
    #print("W: " + str(w))
    #print("target: " + str(target))
    #print("nrMaxTreinos: " + str(nrMaxTreinos))

    while (nrAcertos < NRCASOS and nrTreinamentos <= nrMaxTreinos):

        nrTreinamentos += 1
        nrAcertos = 0
        erro1 = 0.0
        erro2 = 0.0

        for i in range(NRCASOS):  # treinamento

            y = ativacao(x[1][i], x[2][i], w[1], w[2])
            if (y == target[i]):  # comparando y com o target
                nrAcertos += 1
                print(target[i])

            erro1 += (target[i] - y) * x[1][i]
            erro2 += (target[i] - y) * x[2][i]

        print("Treino: " + str(nrTreinamentos) +
            ", acertos: " + str(nrAcertos) + "\n", file=buffer)

        if (nrAcertos == NRCASOS):  # convergiu
            break
        else:  # atualizando os pesos
            w[1] += taxaAprendizado * erro1
            w[2] += taxaAprendizado * erro2
            
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


'''taxaAprendizado = 0.0009  # constante de aprendizado
x = [1, [25, 22, 30, 27, 4, 6, 10, 3], [34, 37, 33, 37, 40, 38, 44, 42]]
w = [0, 85, 75]
target = [-1, -1, -1, -1, 1, 1, 1, 1]  #target
nrMaxTreinos = 5000

teste = treinarPerceptron(taxaAprendizado, x, w, target, nrMaxTreinos)'''