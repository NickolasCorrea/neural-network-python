#NICKOLAS DE SOUZA SILVEIRA CORRÊA - RA: 185823
#VICTOR RICO MOURA SANTOS - RA: 191068

#define NRCASOS 8 #verificar depois o que o define faz

w1 = 87
w2 = 92

def funcao_ativacao(x1, x2):
    net = x1*w1 + x2*w2
    y = -1.0
    if (net >= 0.0):
        y = 1.0
    return (y)

i = 0
passo = 0.0009; #constante de aprendizado

x1[NRCASOS] = {25.0,22.0,30.0,27.0,4.0,6.0,10.0,3.0}
x2[NRCASOS] = {34.0,37.0,33.0,37.0,40.0,38.0,40.0,42.0}
t[NRCASOS] = {-1.0,-1.0,-1.0,-1.0,1.0,1.0,1.0,1.0}; #target

int nr_acertos = 0; #acertos por treinamento
int nr_treinamentos = 0
float erro1=0.0,erro2=0.0

while (1):
    nr_treinamentos++
    nr_acertos=0
    erro1=0.0
    erro2=0.0
    for (i=0;i<NRCASOS;i++) { //treinamento
    float y = funcao_ativacao (x1[i],x2[i]);
    if (y==t[i]) { //comparando y com o target
    nr_acertos++;
    }
    erro1+=(t[i]-y)*x1[i];
    erro2+=(t[i]-y)*x2[i];
    }//fim for
    printf ("Treino: %d, acertos: %d\n",nr_treinamentos,nr_acertos);
    if (nr_acertos==NRCASOS) { //convergiu
    break;
    }
    else { //atualizando os pesos
    w1=w1+passo*erro1;
    w2=w2+passo*erro2;
    }
#fim while

printf ("Pesos Finais: w1: %f, w2: %f, \n",w1,w2);
