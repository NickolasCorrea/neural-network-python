# NICKOLAS DE SOUZA SILVEIRA CORRÊA - RA: 185823
# VICTOR RICO MOURA SANTOS - RA: 191068

def funcao_ativacao(x1, x2):
    net = x1*w[1] + x2*w[2]
    y = -1.0
    if (net >= 0.0):
        y = 1.0
    return y

def treinarPerceptron(taxaAprendizado, x, w, target, nrMaxTreinos):
    
    nrTreinamentos = 0
    nrAcertos = 0  # acertos por treinamento
    erro1 = 0.0
    erro2 = 0.0
    NRCASOS = len(target)

    while (nrAcertos != NRCASOS and nrTreinamentos != nrMaxTreinos):

        nrTreinamentos += 1
        nr_acertos = 0
        erro1 = 0.0
        erro2 = 0.0

        for i in range(NRCASOS):  # treinamento

            y = funcao_ativacao(x[1][i], x[2][i])
            if (y == target[i]):  # comparando y com o target
                nrAcertos += 1

            erro1 += (target[i] - y) * x[1][i]
            erro2 += (target[i] - y) * x[2][i]

        print("Treino: " + str(nrAcertos) +
            ", acertos: " + str(nrAcertos) + "\n")

        if (nr_acertos == NRCASOS):  # convergiu
            break
        else:  # atualizando os pesos
            w[1] += taxaAprendizado * erro1
            w[2] += taxaAprendizado * erro2
            
    if(nrAcertos == NRCASOS):
        print("\nCONVERGIU!")
    else:
        print("\nNÃO CONVERGIU!")
    print("Pesos Finais: w1: " + str(w[1]) + ", w2: " + str(w[2]) + "\n")


taxaAprendizado = 0.0009  # constante de aprendizado
x = [1, [25, 22, 30, 27, 4, 6, 10, 3], [34, 37, 33, 37, 40, 38, 44, 42]]
w = [0, 85, 75]
target = [-1, -1, -1, -1, 1, 1, 1, 1]  #target
nrMaxTreinos = 5000

teste = treinarPerceptron(taxaAprendizado, x, w, target, nrMaxTreinos)