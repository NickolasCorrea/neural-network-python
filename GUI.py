import tkinter
from tkinter import ttk, StringVar, END, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
     FigureCanvasTkAgg)
import numpy as np
import adaline
 
casos = []
idCaso = 1

def adicionaCaso():
    global idCaso

    x1_entrada_valor = x1_entrada.get()
    x2_entrada_valor = x2_entrada.get()

    if (x1_entrada_valor == "" and x2_entrada_valor == ""):
        messagebox.showerror(title = "Entradas vazias", message = "Primeiramente, insira os valores das entradas!")
    elif (x1_entrada_valor == ""):
        messagebox.showerror(title = "X1 vazio", message = "Insira o valor de X1 !")
    elif (x2_entrada_valor == ""):
        messagebox.showerror(title = "X2 vazio", message = "Insira o valor de X2 !")
    elif (not x1_entrada_valor.isnumeric() or not x2_entrada_valor.isnumeric()):
        messagebox.showerror(title = "X2 vazio", message = "Insira apenas valores numericos !")
    else:
        target_radio_valor = target_radio.get()

        # Adiciona novo caso à lista
        casos.append([idCaso, x1_entrada_valor, x2_entrada_valor, target_radio_valor])
        idCaso += 1

        # Insere novo caso na tabela
        tabela.insert(parent = "", index = END, values = (x1_entrada_valor, x2_entrada_valor, target_radio_valor))

        x1_entrada.delete(0, END)
        x2_entrada.delete(0, END)

def deletaCasos(_):
    for linha in tabela.selection():
        for caso in casos:
            if (caso[0] == int(linha[1:])):
                casos.remove(caso)
                break
        tabela.delete(linha)
    
def verificaPreenchimentoEntradas():
    w1_entrada_valor = w1_entrada.get()
    w2_entrada_valor = w2_entrada.get()

    x0_entrada_valor = x0_entrada.get()
    w0_entrada_valor = w0_entrada.get()

    taxaAprendizagem_entrada_valor = taxaAprendizagem_entrada.get()
    numMaxTreinos_entrada_valor = numMaxTreinos_entrada.get()

    modeloRede_radio_valor = modeloRede_radio.get()

    # Verifica o preenchimento dos pesos W1 e W2
    if (w1_entrada_valor == "" and w2_entrada_valor == ""):
       messagebox.showerror(title = "Pesos vazios", message = "Primeiramente, insira os valores dos pesos iniciais! (W1 e W2)")
    elif (w1_entrada_valor == ""):
        messagebox.showerror(title = "W1 vazio", message = "Insira o valor de W1 !")
    elif (w2_entrada_valor == ""):
        messagebox.showerror(title = "W2 vazio", message = "Insira o valor de W2 !")

    # Verifica o preenchimento do bias X0 e W0
    elif (x0_entrada_valor == "" and w0_entrada_valor == ""):
       messagebox.showerror(title = "Bias vazio", message = "Primeiramente, preencha os valores do Bias! (X0 e W0)")
    elif (x0_entrada_valor == ""):
        messagebox.showerror(title = "XO vazio", message = "Insira o valor de X0 !")
    elif (w0_entrada_valor == ""):
        messagebox.showerror(title = "W0 vazio", message = "Insira o valor de W0 !")

    # Verifica o preenchimento da taxa de aprendizagem e numero máximo de treinos
    elif (taxaAprendizagem_entrada_valor == ""):
        messagebox.showerror(title = "Taxa de aprendizagem vazio", message = "Insira o valor da taxa de aprendizagem !")
    else:
    
        # Verifica o preenchimento do numero máximo de treinos
        if (numMaxTreinos_entrada_valor == ""):
            numMaxTreinos_entrada_valor = 100000

        # Envia os dados das entradas para a função de treino
        x1 = []
        x2 = []
        target = []
        for caso in casos:
            x1.append(int(caso[1]))
            x2.append(int(caso[2]))
            target.append(int(caso[3]))
        
        xTotal = [x0_entrada_valor, x1, x2]
        wTotal = [w0_entrada_valor, w1_entrada_valor, w2_entrada_valor]
        if(modeloRede_radio_valor == "Adaline"):
            adaline.treinarAdaline(taxaAprendizagem_entrada_valor, xTotal, wTotal,
                                    target, numMaxTreinos_entrada_valor)

            # Depois de realizar o cálculo, deve-se desenhar no gráfico, e recarregar o desenho.
            #t = np.arange(0, 2*np.pi, .01)
            #ax.plot(t, np.sin(t))
            #canvas.draw()
        #else:
            #perceptron.treinarPerceptron(taxaAprendizagem_entrada_valor, [x0_entrada_valor, x1, x2], [w0_entrada_valor, w1_entrada_valor, w2_entrada_valor], 
            # target, numMaxTreinos_entrada_valor)


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
treinoNeuronio_frame.grid(row = 0, column = 2, padx = (90, 20), pady = 20, sticky = "w")

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

# Criando Grid para o MODELOS DE REDES NEURAIS
modeloRede_frame = ttk.LabelFrame(frame, text = "Treino de Neurônios")
modeloRede_frame.grid(row = 0, column = 3, padx = (90, 20), pady = 20, sticky = "w")

# Seta o modeloRede_radio para começar com ADALINE por padrão
modeloRede_radio = StringVar(value = "Adaline")

# Criando radio button para target +1
perceptron_radioButton = ttk.Radiobutton(modeloRede_frame, text = "Perceptron", value = "Perceptron", variable = modeloRede_radio)
perceptron_radioButton.grid(row = 1, column = 1)

# Criando radio button para target -1
adaline_radioButton = ttk.Radiobutton(modeloRede_frame, text = "Adaline", value = "Adaline", variable = modeloRede_radio)
adaline_radioButton.grid(row = 1, column = 2)

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
target_radio = StringVar(value = "+1")

# Criando radio button para target +1
targetMais_button = ttk.Radiobutton(casos_frame, text = "+1", value = "+1", variable = target_radio)
targetMais_button.grid(row = 1, column = 1)

# Criando radio button para target -1
targetMenos_button = ttk.Radiobutton(casos_frame, text = "-1", value = "-1", variable = target_radio)
targetMenos_button.grid(row = 1, column = 2)

saveButton = ttk.Button(casos_frame, text = "Salvar", command = adicionaCaso)
saveButton.grid(row = 0, column = 5)

# Criando um padding para todos os conteudos dentro do frame casos_frame
for widget in casos_frame.winfo_children():
    widget.grid_configure(padx = 5, pady = 5)

# Criando a tabela de casos
tabela = ttk.Treeview(frame, columns = ("x1", "x2",  "target"), show = "headings", height = 19)
tabela.column("x1", width = 150)
tabela.column("x2", width = 150)
tabela.column("target", width = 150)
tabela.heading("x1", text = "X1")
tabela.heading("x2", text = "X2")
tabela.heading("target", text = "Target")
tabela.grid(row = 3, column =  0, columnspan = 2, padx = 20, pady = 20)

# Ajusta padding left da label de X2 e do botão salvar
x2_label.grid(padx = (15, 5))
saveButton.grid(padx = (15, 5))

tabela.bind("<Delete>", deletaCasos)

#-------------------------------------------------------------------------

# Cria o grafico_frame como um LabelFrame
grafico_frame = ttk.LabelFrame(frame, text="Gráfico")
grafico_frame.grid(row=1, rowspan = 7, columnspan = 2, column=2, padx=20, pady=20)

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