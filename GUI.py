import tkinter as tk
from tkinter import ttk, StringVar, END, messagebox, Text, DISABLED, filedialog as fd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
     FigureCanvasTkAgg)
from tkscrolledframe import ScrolledFrame

import adaline
import perceptron
 

casos = []
idCaso = 1


def adicionaCaso(editar):
    global idCaso

    x1_entrada_valor = x1_entrada.get().replace(",", ".", 1)
    x2_entrada_valor = x2_entrada.get().replace(",", ".", 1)

    if (x1_entrada_valor == "" and x2_entrada_valor == ""):
        messagebox.showerror(title = "Entradas vazias", message = "Primeiramente, insira os valores das entradas!")
    elif (x1_entrada_valor == ""):
        messagebox.showerror(title = "X1 vazio", message = "Insira o valor de X1 !")
    elif (x2_entrada_valor == ""):
        messagebox.showerror(title = "X2 vazio", message = "Insira o valor de X2 !")
    elif (not is_number(x1_entrada_valor) or not is_number(x2_entrada_valor)):
        messagebox.showerror(title = "Valores não numéricos", message = "Insira apenas valores numéricos !")
    else:
        target_radio_valor = int(target_radio.get())
        x1_entrada_valor = int(float(x1_entrada_valor))
        x2_entrada_valor = int(float(x2_entrada_valor))

        if (not editar):
            # Adiciona novo caso à lista
            casos.append([idCaso, x1_entrada_valor, x2_entrada_valor, target_radio_valor])
            idCaso += 1

            # Insere novo caso na tabela
            tabela.insert(parent = "", index = END, values = (x1_entrada_valor, x2_entrada_valor, target_radio_valor))
        else:
            if (len(tabela.selection()) == 0):
                messagebox.showerror(title = "Item não selecionado", message = "Seleciona uma das linhas !")
                return
            linha = tabela.selection()[0]
            for caso in casos:
                if (caso[0] == int(linha[1:], base=16)):
                    caso[1] = x1_entrada_valor
                    caso[2] = x2_entrada_valor
                    caso[3] = target_radio_valor
                    break
            tabela.item(linha, values=(x1_entrada_valor, x2_entrada_valor, target_radio_valor))

        x1_entrada.delete(0, END)
        x2_entrada.delete(0, END)

def preencheCampos(_):
    global target_radio

    try:
        valoresLinha = tabela.item(tabela.selection()[0], "values")
        x1_entrada.delete(0, END)
        x2_entrada.delete(0, END)
        x1_entrada.insert(0, valoresLinha[0])
        x2_entrada.insert(0, valoresLinha[1])
        if (valoresLinha[2] == "1"):
            targetMais_button.invoke()
        else:
            targetMenos_button.invoke()
    except IndexError:
        return


def deletaCasos(_):
    for linha in tabela.selection():
        for caso in casos:
            if (caso[0] == int(linha[1:], base=16)):
                casos.remove(caso)
                break
        tabela.delete(linha)

def alteraEstadoBias():
    if (modeloRede_radio.get() == "Adaline"):
        x0_entrada.config(state = "normal")
        w0_entrada.config(state = "normal")
    else:
        x0_entrada.config(state = DISABLED)
        w0_entrada.config(state = DISABLED)

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def leArquivo():
    global idCaso, casos

    messagebox.showinfo(title = "Instruções de formatação", message = "Selecione um arquivo em que os valores de X1 estão na primeira linha, de X2 na segunda, e de target na terceira.\nOs valores devem ser separados por vírgula.")
    caminho = fd.askopenfilename()
    arquivo = open(caminho, "r")
    casosArquivo = arquivo.read().split("\n")
    arquivo.close()

    x1 = casosArquivo[0].split(",")
    x2 = casosArquivo[1].split(",")
    target = casosArquivo[2].split(",")
    try:
        x1 = list(map(int, x1))
        x2 = list(map(int, x2))
        target = list(map(int, target))
    except ValueError:
        messagebox.showerror(title = "Formatação incorreta", message = "Siga as instruções de formatação !")
        return
    
    if (len(x1) == len(x2) and len(x1) == len(target)):
        casos = []
        tabela.delete(*tabela.get_children())

        for contador in range(len(x1)):
            tabela.insert(parent = "", index = END, values = (x1[contador], x2[contador], target[contador]))
            casos.append([idCaso, x1[contador], x2[contador], target[contador]])
            idCaso += 1
            
    else:
        messagebox.showerror(title = "Inconsistência no número de casos", message = "Número de valores entre X1, X2 e target é diferente !")
    
def verificaPreenchimentoEntradas():
    global casos

    modeloRede_radio_valor = modeloRede_radio.get()

    w1_entrada_valor = w1_entrada.get().replace(",", ".", 1)
    w2_entrada_valor = w2_entrada.get().replace(",", ".", 1)

    x0_entrada_valor = "1"
    w0_entrada_valor = "0"
    if (modeloRede_radio_valor == "Adaline"):
        x0_entrada_valor = x0_entrada.get().replace(",", ".", 1)
        w0_entrada_valor = w0_entrada.get().replace(",", ".", 1)

    taxaAprendizagem_entrada_valor = taxaAprendizagem_entrada.get().replace(",", ".", 1)
    numMaxTreinos_entrada_valor = numMaxTreinos_entrada.get().replace(",", ".", 1)

    # Verifica o preenchimento do numero máximo de treinos
    if (numMaxTreinos_entrada_valor == ""):
        numMaxTreinos_entrada_valor = 100000

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
    
    elif (not is_number(x0_entrada_valor) or not is_number(w0_entrada_valor) or not is_number(w1_entrada_valor) or
           not is_number(w2_entrada_valor) or not is_number(taxaAprendizagem_entrada_valor) or
             not is_number(numMaxTreinos_entrada_valor)):
        messagebox.showerror(title = "Valores não numéricos", message = "Insira apenas valores numéricos !")
    else:

        # Envia os dados das entradas para a função de treino
        x1 = []
        x2 = []
        target = []
        for caso in casos:
            x1.append(caso[1])
            x2.append(caso[2])
            target.append(caso[3])

        x0_entrada_valor = int(float(x0_entrada_valor))
        xLista = [x0_entrada_valor, x1, x2]

        wLista = [w0_entrada_valor, w1_entrada_valor, w2_entrada_valor]
        wLista = list(map(float, wLista))

        taxaAprendizagem_entrada_valor = float(taxaAprendizagem_entrada_valor)

        if (modeloRede_radio_valor == "Adaline"):
            resultado = adaline.treinarAdaline(taxaAprendizagem_entrada_valor, xLista, wLista,
                                    target, int(float(numMaxTreinos_entrada_valor)))
            
            # Deleta o texto na área de log (LIMPAR)
            logArea.delete("1.0", "end")
            # Insere o texto inicial na área de log
            logArea.insert("1.0", resultado)
            # Faz o Tkinter focar no fim do texto
            logArea.see(END)

            plt.clf()
            # Depois de realizar o cálculo, deve-se desenhar no gráfico, e recarregar o desenho.
            x1_azul = [x1[i] for i in range(len(x1)) if target[i] == -1]
            x2_azul = [x2[i] for i in range(len(x2)) if target[i] == -1]

            x1_verde = [x1[i] for i in range(len(x1)) if target[i] == 1]
            x2_verde = [x2[i] for i in range(len(x2)) if target[i] == 1]

            # Plotar os pontos de x1 (azuis)
            plt.scatter(x1_azul, x2_azul, color='blue', label='X1 (-1)')

            # Plotar os pontos de x2 (verdes)
            plt.scatter(x1_verde, x2_verde, color='green', label='X2 (1)')
            canvas.draw()

        else:
            resultado = perceptron.treinarPerceptron(taxaAprendizagem_entrada_valor, xLista, wLista, 
            target, int(float(numMaxTreinos_entrada_valor)))

            # Deleta o texto na área de log (LIMPAR)
            logArea.delete("1.0", "end")
            # Insere o texto inicial na área de log
            logArea.insert("1.0", resultado)
            # Faz o Tkinter focar no fim do texto
            logArea.see(END)

            plt.clf()
            # Depois de realizar o cálculo, deve-se desenhar no gráfico, e recarregar o desenho.
            x1_azul = [x1[i] for i in range(len(x1)) if target[i] == -1]
            x2_azul = [x2[i] for i in range(len(x2)) if target[i] == -1]

            x1_verde = [x1[i] for i in range(len(x1)) if target[i] == 1]
            x2_verde = [x2[i] for i in range(len(x2)) if target[i] == 1]

            # Plotar os pontos de x1 (azuis)
            plt.scatter(x1_azul, x2_azul, color='blue', label='X1 (-1)')

            # Plotar os pontos de x2 (verdes)
            plt.scatter(x1_verde, x2_verde, color='green', label='X2 (1)')
            canvas.draw()

#-------------------------------------------------------------------------

# Criando janela da aplicação
window = tk.Tk()
window.geometry("1187x600")
window.title("Rede Neural Adaline")
# window.state('zoomed') --> Começa a aplicação em tela cheia.

# Criando frame que comportará os grids
frame_scroll = ScrolledFrame(window)
frame_scroll.pack(side="top", expand=True, fill="both")
frame_scroll.bind_arrow_keys(window)
frame_scroll.bind_scroll_wheel(window)

frame = frame_scroll.display_widget(ttk.Frame)

style = ttk.Style()

# Criando Grid dos PESOS
pesos_frame = ttk.LabelFrame(frame, text = "Insira os pesos iniciais")
pesos_frame.grid(row = 0, column = 0, padx = (17, 0), pady = 10, sticky = "w")

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
bias_frame.grid(row = 0, column = 1, padx = (0, 51), pady = 10, sticky = "e")

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
treinoNeuronio_frame.grid(row = 0, column = 2, padx = (38, 0), pady = 10, sticky = "w")

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
modeloRede_frame = ttk.LabelFrame(frame, text = "Modo de treinamento")
modeloRede_frame.grid(row = 0, column = 3, padx = (60, 0), pady = 10)

# Seta o modeloRede_radio para começar com ADALINE por padrão
modeloRede_radio = StringVar(value = "Adaline")

style.configure("bold.TRadiobutton", font=("Helvetica", "14", "bold"))
# Criando radio button para Perceptron
perceptron_radioButton = ttk.Radiobutton(modeloRede_frame, text = "Perceptron", value = "Perceptron", variable = modeloRede_radio, command = alteraEstadoBias, style = "bold.TRadiobutton")
perceptron_radioButton.grid(row = 1, column = 1)

# Criando radio button para Adaline
adaline_radioButton = ttk.Radiobutton(modeloRede_frame, text = "Adaline", value = "Adaline", variable = modeloRede_radio, command = alteraEstadoBias, style = "bold.TRadiobutton")
adaline_radioButton.grid(row = 1, column = 2)

# Criando um padding para todos os conteudos dentro do frame casos_frame
for widget in modeloRede_frame.winfo_children():
    widget.grid_configure(padx = 5, pady = 5)

#-------------------------------------------------------------------------

# Criando Grid para os CASOS
casos_frame = ttk.LabelFrame(frame, text = "Casos")
casos_frame.grid(row = 1, column =  0, columnspan = 2, padx = (14, 22), pady = 10)

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

saveButton = ttk.Button(casos_frame, text = "Salvar", command = lambda: adicionaCaso(False))
saveButton.grid(row = 0, column = 5)

editButton = ttk.Button(casos_frame, text = "Editar", command = lambda: adicionaCaso(True))
editButton.grid(row = 1, column = 5)

# Criando um padding para todos os conteudos dentro do frame casos_frame
for widget in casos_frame.winfo_children():
    widget.grid_configure(padx = 5, pady = 5)

# Criando botão para abrir arquivo
abrirArquivo_button = ttk.Button(frame, text = "Abrir arquivo", command = leArquivo)
abrirArquivo_button.grid(row = 2, column = 0, columnspan = 2)

# Criando a TABELA DE CASOS
tabela = ttk.Treeview(frame, columns = ("x1", "x2",  "target"), show = "headings", height = 18)
tabela.column("x1", width = 154)
tabela.column("x2", width = 154)
tabela.column("target", width = 152)
tabela.heading("x1", text = "X1")
tabela.heading("x2", text = "X2")
tabela.heading("target", text = "Target")
tabela.grid(row = 3, column =  0, columnspan = 2, padx = (17, 0), pady = 10, sticky = "w")

# Ajusta padding left da label de X2 e do botão salvar
x2_label.grid(padx = (15, 5))
saveButton.grid(padx = (15, 5))
editButton.grid(padx = (15, 5))

tabela.bind("<<TreeviewSelect>>", preencheCampos)
tabela.bind("<Delete>", deletaCasos)

#-------------------------------------------------------------------------

# Cria o grafico_frame como um LabelFrame
grafico_frame = ttk.LabelFrame(frame, text="Gráfico")
grafico_frame.grid(row=1, rowspan = 3, columnspan = 2, column=2, padx=10, pady=10)

# Cria o botão "Treinar um Neurônio" como um LabelFrame
trainNeuronButton = ttk.Button(grafico_frame, padding=(10, 0), text = "Treinar Neurônio", 
                               command = verificaPreenchimentoEntradas)
trainNeuronButton.grid(row = 0, column = 0)

# Cria a figura e os seus eixos
fig, ax = plt.subplots()

# Adiciona a figura ao grafico_frame
canvas = FigureCanvasTkAgg(fig, master=grafico_frame)
plt.title('Gráfico de Dispersão', fontweight='bold')
plt.xlabel('X1', fontweight='bold')
plt.ylabel('X2', fontweight='bold')
canvas.get_tk_widget().grid(row = 1, column = 0)
canvas.draw()

# Configura a expansão dos widgets
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
grafico_frame.columnconfigure(0, weight=1)
grafico_frame.rowconfigure(0, weight=1)

#-------------------------------------------------------------------------

# Criando Grid para o LOG
log_frame = ttk.LabelFrame(frame, text="Log")
log_frame.grid(row = 5, column = 0, columnspan = 5, padx = 16, pady = 10, sticky = "w")

logArea=Text(log_frame, height = 8, width = 141)
logArea.grid(row = 2, column =  0)

# Loop para a GUI rodar até que seja fechada
window.mainloop()