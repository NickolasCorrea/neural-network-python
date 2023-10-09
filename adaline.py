#NICKOLAS DE SOUZA SILVEIRA CORRÊA - RA: 185823
#VICTOR RICO MOURA SANTOS - RA: 191068

from math import sqrt

def funcao_ativacao(x1, x2):
    saidaIntermediaria = (x[0]*w[0]) + (x1*w[1]) + (x2*w[2])
    saida = -1.0
    if (saidaIntermediaria >= 0.0):
        saida = 1.0
    return saidaIntermediaria, saida


# x1 = [25, 22, 30, 27, 4, 6, 10, 3]
# x2 = [34, 37, 33, 37, 40, 38, 44, 42]
# target = [-1, -1, -1, -1, 1, 1, 1, 1]  #target
# x1 = [2]
# x2 = [31]
NRCASOS = 8
x = [1, [25, 22, 30, 27, 4, 6, 10, 3], [34, 37, 33, 37, 40, 38, 44, 42]]
w = [0, 0.02, 0.01]
target = [-1, -1, -1, -1, 1, 1, 1, 1]  #target
# x = [1, [2], [31]]
# w = [0, 4, -12]
# target = [1]  #target

# x0 = 1
# w0 = 0
# w1 = 4
# w2 = -12

taxaAprendizado = 0.0001  # constante de aprendizado (0 < taxaAprendizado < 2)
nrAcertos = 0  # acertos por treinamento
nrTreinamentos = 0
erro = 0

while (1):
    nrTreinamentos += 1
    nrAcertos = 0

    contador = 0
    for contador in range(NRCASOS):
        
        saidaIntermediaria, saida = funcao_ativacao(x[1][contador], x[2][contador])
        if (saida == target[contador]):
            nrAcertos += 1

        print("Treino: " + str(nrTreinamentos) + ", acertos: " + str(nrAcertos))
        
        if (nrAcertos == NRCASOS):  # convergiu
            break
        else:
            erro = target[contador] - abs(saidaIntermediaria)
            # xQuadrado = (x[0]**2 + x[1][contador]**2 + x[2][contador]**2)
            xQuadrado = x[0]**2
            for num in range(1, len(x)):
                xQuadrado += x[num][contador]**2

            w[0] += taxaAprendizado * erro * x[0] / xQuadrado
            w[1] += taxaAprendizado * erro * x[1][contador] / xQuadrado
            w[2] += taxaAprendizado * erro * x[2][contador] / xQuadrado
            print("Erro: " + str(erro))
            print("Saida Intermediária: " + str(saidaIntermediaria) + "\n")

print("Pesos Finais: w1: " + str(w[1]) + ", w2: " + str(w[2]) + ", w0: " + str(w[0]) + ", \n")
