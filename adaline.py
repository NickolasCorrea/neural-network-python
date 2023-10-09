#NICKOLAS DE SOUZA SILVEIRA CORRÊA - RA: 185823
#VICTOR RICO MOURA SANTOS - RA: 191068

def funcao_ativacao(x1, x2):
    net = x1*w1 + x2*w2
    y = -1.0
    if (net >= 0.0):
        y = 1.0
    return y

NRCASOS = 8  #verificar depois o que o define faz
w1 = 85
w2 = 75
i = 0
taxa = 0.0009  # constante de aprendizado

x1 = [25,22,30,27,4,6,10,3]
x2 = [34,37,33,37,40,38,44,42]
t = [-1,-1,-1,-1,1,1,1,1]  #target

nr_acertos = 0  #acertos por treinamento
nr_treinamentos = 0
erro = 0

while (1):
    nr_treinamentos += 1
    nr_acertos = 0
    
    for i in range(NRCASOS):
        
        y = funcao_ativacao(x1[i], x2[i])
        if (y == t[i]):  # comparando y com o target
            nr_acertos += 1
            print(i)
        erro = t[i] - y
    
    print("Treino: " + str(nr_treinamentos) + ", acertos: " + str(nr_acertos) + "\n")

    if (nr_acertos == NRCASOS):  #convergiu
        break
    else:
        w1 += taxa * erro * x1[i] / (abs(x1[i])**2)
        w2 += taxa * erro * x1[i] / (abs(x1[i])**2)

print("Pesos Finais: w1: " + str(w1) + ", w2: " + str(w2) + ", \n")
