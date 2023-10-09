#NICKOLAS DE SOUZA SILVEIRA CORRÊA - RA: 185823
#VICTOR RICO MOURA SANTOS - RA: 191068

def funcao_ativacao(x1, x2):
    saidaIntermediaria = (x0*w0) + (x1*w1) + (x2*w2)
    saida = -1.0
    if (saidaIntermediaria >= 0.0):
        saida = 1.0
    return saidaIntermediaria, saida


# x1 = [25, 22, 30, 27, 4, 6, 10, 3]
# x2 = [34, 37, 33, 37, 40, 38, 44, 42]
# target = [-1, -1, -1, -1, 1, 1, 1, 1]  #target
NRCASOS = 2
x1 = [30, 10]
x2 = [33, 44]
target = [-1, 1]  #target

x0 = 1
w0 = 0
w1 = 0.02
w2 = 0.01

taxaAprendizado = 0.0001  # constante de aprendizado (0 < taxaAprendizado < 2 )
nrAcertos = 0  # acertos por treinamento
nrTreinamentos = 0
erro = 0

while (1):
    nrTreinamentos += 1
    nrAcertos = 0

    contador = 0
    for contador in range(NRCASOS):
        
        saidaIntermediaria, saida = funcao_ativacao(x1[contador], x2[contador])
        if (saida == target[contador]):
            nrAcertos += 1
            print("Contador: " + str(contador))
        erro = target[contador] - saidaIntermediaria
    
    print("Treino: " + str(nrTreinamentos) + ", acertos: " + str(nrAcertos) + "\n")
    print("Saida Intermediaria: " + str(saidaIntermediaria))

    if (nrAcertos == NRCASOS):  # convergiu
        break
    else:
        w0 += taxaAprendizado * erro * x0 / (abs(x0)**2)
        w1 += taxaAprendizado * erro * x1[contador] / (abs(x1[contador])**2)
        w2 += taxaAprendizado * erro * x2[contador] / (abs(x2[contador])**2)

print("Pesos Finais: w1: " + str(w1) + ", w2: " + str(w2) + ", \n")
