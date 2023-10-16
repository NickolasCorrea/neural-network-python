import tkinter
from tkinter import ttk, StringVar, END, messagebox, DISABLED
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
     FigureCanvasTkAgg)
import numpy as np
#import adaline
 
casos = []

def criaTabela():
    x1_entrada_valor = x1_entrada.get()
    x2_entrada_valor = x2_entrada.get()

    if (x1_entrada_valor == "" and x2_entrada_valor == ""):
        messagebox.showerror(title = "Entradas vazias", message = "Primeiramente, insira os valores das entradas!")
    elif (x1_entrada_valor == ""):
        messagebox.showerror(title = "X1 vazio", message = "Insira o valor de X1 !")
    elif (x2_entrada_valor == ""):
        messagebox.showerror(title = "X2 vazio", message = "Insira o valor de X2 !")
    else:
        # Criando Grid para a tabela de casos
        tabela_frame = ttk.LabelFrame(frame, text = "Tabela de casos")
        tabela_frame.grid(row = 3, column =  0, columnspan = 2, padx = 20, pady = 20)

        # Adiciona primeira linha
        header = ["X1", "X2", "Target"]
        for contador in range(3):
            tabela_entrada = ttk.Entry(tabela_frame)
            tabela_entrada.grid(row = 0, column = contador)
            tabela_entrada.insert(END, header[contador])
            tabela_entrada.config(state = DISABLED)
        
        # Adiciona novo caso à lista
        casos.append([x1_entrada_valor, x2_entrada_valor, target_valor.get()])

        # Monta tabela
        for linha in range(len(casos)):
            for coluna in range(len(casos[0])):
                tabela_entrada = ttk.Entry(tabela_frame)
                tabela_entrada.grid(row = linha + 1, column = coluna)
                tabela_entrada.insert(END, casos[linha][coluna])
                tabela_entrada.config(state = DISABLED)

        # Limpa entradas
        x1_entrada.delete(0, END)
        x2_entrada.delete(0, END)


    
def verificaPreenchimentoEntradas():
    w1_entrada_valor = w1_entrada.get()
    w2_entrada_valor = w2_entrada.get()

    x0_entrada_valor = x0_entrada.get()
    w0_entrada_valor = w0_entrada.get()

    taxaAprendizagem_entrada_valor = taxaAprendizagem_entrada.get()
    numMaxTreinos_entrada_valor = numMaxTreinos_entrada.get()

    # Verifica o preenchimento dos pesos W1 e W2
    if (w1_entrada_valor == "" and w2_entrada_valor == ""):
       messagebox.showerror(title = "Pesos vazios", message = "Primeiramente, insira os valores dos pesos iniciais! (W1 e W2)")
    elif (w1_entrada_valor == ""):
        messagebox.showerror(title = "W1 vazio", message = "Insira o valor de W1 !")
    elif (w2_entrada_valor == ""):
        messagebox.showerror(title = "W2 vazio", message = "Insira o valor de W2 !")

    # Verifica o preenchimento do bias X0 e W0
    if (x0_entrada_valor == "" and w0_entrada_valor == ""):
       messagebox.showerror(title = "Bias vazio", message = "Primeiramente, preencha os valores do Bias! (X0 e W0)")
    elif (x0_entrada_valor == ""):
        messagebox.showerror(title = "XO vazio", message = "Insira o valor de X0 !")
    elif (w0_entrada_valor == ""):
        messagebox.showerror(title = "W0 vazio", message = "Insira o valor de W0 !")

    # Verifica o preenchimento da taxa de aprendizagem e numero máximo de treinos
    if (taxaAprendizagem_entrada_valor == ""):
        messagebox.showerror(title = "Taxa de aprendizagem vazio", message = "Insira o valor da taxa de aprendizagem !")
    
    # Verifica o preenchimento do numero máximo de treinos
    if (numMaxTreinos_entrada_valor == ""):
        numMaxTreinos_entrada_valor = 100000

    # Envia os dados das entradas para a função de treino
    #adaline.treinarAdaline()

    # Depois de realizar o cálculo, deve-se desenhar no gráfico, e recarregar o desenho.
    #t = np.arange(0, 2*np.pi, .01)
    #ax.plot(t, np.sin(t))
    #canvas.draw()

#-------------------------------------------------------------------------

# Criando janela da aplicação
window = tkinter.Tk()
window.title("Rede Neural Adaline")
# window.state('zoomed') --> Começa a aplicação em tela cheia.

# Criando frame que comportará os grids
frame = ttk.Frame(window)
frame.pack()

# Criando Grid dos PESOS
pesos_frame = ttk.LabelFrame(frame, text = "Insira os pesos iniciais")
pesos_frame.grid(row = 0, column = 0, padx = 20, pady = 20, sticky = "w")

# Criando label para o W1
w1_label = ttk.Label(pesos_frame, text= "W1:")
w1_label.grid(row = 0, column = 0)
# Criando entrada para o W1
w1_entrada = ttk.Entry(pesos_frame)
w1_entrada.grid(row = 0, column = 1)

# Criando label para o W2
w2_label = ttk.Label(pesos_frame, text= "W2:")
w2_label.grid(row = 1, column = 0)
# Criando entrada para o W2
w2_entrada = ttk.Entry(pesos_frame)
w2_entrada.grid(row = 1, column = 1)

# Criando um padding para todos os conteudos dentro do frame pesos_frame
for widget in pesos_frame.winfo_children():
    widget.grid_configure(padx = 5, pady = 5)

#-------------------------------------------------------------------------

# Criando Grid para o BIAS
bias_frame = ttk.LabelFrame(frame, text = "Bias")
bias_frame.grid(row = 0, column = 1, padx = 20, pady = 20, sticky = "e")

# Criando label para o X0
x0_label = ttk.Label(bias_frame, text= "X0:")
x0_label.grid(row = 0, column = 0)
# Criando entrada para o X0
x0_entrada = ttk.Entry(bias_frame)
x0_entrada.grid(row = 0, column = 1)

# Criando label para o w0
w0_label = ttk.Label(bias_frame, text= "W0:")
w0_label.grid(row = 1, column = 0)
# Criando entrada para o w0
w0_entrada = ttk.Entry(bias_frame)
w0_entrada.grid(row = 1, column = 1)

# Criando um padding para todos os conteudos dentro do frame bias_frame
for widget in bias_frame.winfo_children():
    widget.grid_configure(padx = 5, pady = 5)

#-------------------------------------------------------------------------

# Criando Grid para o TREINO DOS NEURONIOS
treinoNeuronio_frame = ttk.LabelFrame(frame, text = "Treino de Neurônios")
treinoNeuronio_frame.grid(row = 0, column = 2, padx = (95, 20), pady = 20)

# Criando label para a taxa de aprendizagem
taxaAprendizagem_label = ttk.Label(treinoNeuronio_frame, text= "Taxa de aprendizagem: ")
taxaAprendizagem_label.grid(row = 0, column = 0)
# Criando entrada para a taxa de aprendizagem
taxaAprendizagem_entrada = ttk.Entry(treinoNeuronio_frame)
taxaAprendizagem_entrada.grid(row = 0, column = 1)

# Criando label para o numero max de treinos
numMaxTreinos_label = ttk.Label(treinoNeuronio_frame, text= "Nº Máximo de treinos: ")
numMaxTreinos_label.grid(row = 1, column = 0)
# Criando entrada para o numero max de treinos
numMaxTreinos_entrada = ttk.Entry(treinoNeuronio_frame)
numMaxTreinos_entrada.grid(row = 1, column = 1)

# Criando um padding para todos os conteudos dentro do frame treinoNeuronio_frame
for widget in treinoNeuronio_frame.winfo_children():
    widget.grid_configure(padx = 5, pady = 5)

#-------------------------------------------------------------------------

# Criando Grid para os CASOS
casos_frame = ttk.LabelFrame(frame, text = "Casos")
casos_frame.grid(row = 1, column =  0, columnspan = 2, padx = 20, pady = 20)

# Criando label para o X1
x1_label = ttk.Label(casos_frame, text = "X1:", anchor = "e", width = 6)
x1_label.grid(row = 0, column = 0)
# Criando entrada para o X1
x1_entrada = ttk.Entry(casos_frame)
x1_entrada.grid(row = 0, column = 1, columnspan = 2)

# Criando label para o X2
x2_label = ttk.Label(casos_frame, text= "X2:")
x2_label.grid(row = 0, column = 3)
# Criando entrada para o X2
x2_entrada = ttk.Entry(casos_frame)
x2_entrada.grid(row = 0, column = 4)

# Criando label para target
target_label = ttk.Label(casos_frame, text = "Target:")
target_label.grid(row = 1, column = 0)
target_valor = StringVar(value = "+1")

# Criando radio button para target +1
targetMais_button = ttk.Radiobutton(casos_frame, text = "+1", value = "+1", variable = target_valor)
targetMais_button.grid(row = 1, column = 1)

# Criando radio button para target -1
targetMenos_button = ttk.Radiobutton(casos_frame, text = "-1", value = "-1", variable = target_valor)
targetMenos_button.grid(row = 1, column = 2)

saveButton = ttk.Button(casos_frame, text = "Salvar", command = criaTabela)
saveButton.grid(row = 0, column = 5)

# Criando um padding para todos os conteudos dentro do frame casos_frame
for widget in casos_frame.winfo_children():
    widget.grid_configure(padx = 5, pady = 5)

# Ajusta padding left da label de X2 e do botão salvar
x2_label.grid(padx = (15, 5))
saveButton.grid(padx = (15, 5))

#-------------------------------------------------------------------------

# Cria o grafico_frame como um LabelFrame
grafico_frame = ttk.LabelFrame(frame, text="Gráfico")
grafico_frame.grid(row=1, column=2, padx=20, pady=20)

# Cria o botão "Treinar um Neurônio" como um LabelFrame
trainNeuronButton = ttk.Button(grafico_frame, padding=(5, 5), text = "Treinar Neurônio", 
                               command = verificaPreenchimentoEntradas)
trainNeuronButton.grid(row = 0, column = 0, padx=(0, 500))

# Cria a figura e os seus eixos
fig, ax = plt.subplots()

# Adiciona a figura ao grafico_frame
canvas = FigureCanvasTkAgg(fig, master=grafico_frame)
canvas.get_tk_widget().grid(row = 1, column = 0)
canvas.draw()

# Plot data on Matplotlib Figure
# t = np.arange(0, 2*np.pi, .01)
# ax.plot(t, np.sin(t))

# Configura a expansão dos widgets
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
grafico_frame.columnconfigure(0, weight=1)
grafico_frame.rowconfigure(0, weight=1)


# Loop para a GUI rodar até que seja fechada
window.mainloop()