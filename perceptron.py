#NICKOLAS DE SOUZA SILVEIRA CORRÊA - RA: 185823
#VICTOR RICO MOURA SANTOS - RA: 191068

NRCASOS = 8  #verificar depois o que o define faz

w1 = 87
w2 = 92

def funcao_ativacao(x1, x2):
    net = x1*w1 + x2*w2
    y = -1.0
    if (net >= 0.0):
        y = 1.0
    return y

i = 0
passo = 0.0009  #constante de aprendizado

x1 = {25.0,22.0,30.0,27.0,4.0,6.0,10.0,3.0}
x2 = {34.0,37.0,33.0,37.0,40.0,38.0,40.0,42.0}
t = {-1.0,-1.0,-1.0,-1.0,1.0,1.0,1.0,1.0}  #target

nr_acertos = 0  #acertos por treinamento
nr_treinamentos = 0
erro1 = 0.0
erro2=0.0

while (1):
    nr_treinamentos += 1
    nr_acertos = 0
    erro1 = 0.0
    erro2 = 0.0

    for i in range(NRCASOS):  #treinamento
        y = funcao_ativacao (x1[i],x2[i]);
        if (y == t[i]):  #comparando y com o target
            nr_acertos += 1;

        erro1 += (t[i]-y)*x1[i];
        erro2 += (t[i]-y)*x2[i];
    
    print("Treino: " + str(nr_treinamentos) + ", acertos: " + str(nr_acertos) + "\n");

    if (nr_acertos == NRCASOS):  #convergiu
        break
    else:  #atualizando os pesos
        w1 += passo * erro1;
        w2 += passo * erro2;

print("Pesos Finais: w1: " + str(w1) + ", w2: " + str(w2) + ", \n");
