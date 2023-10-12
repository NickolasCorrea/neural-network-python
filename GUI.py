import tkinter
from tkinter import ttk

# Criando janela da aplicação
window = tkinter.Tk()
window.title("Rede Neural Adaline")

# Criando frame que comportará os grids
frame = tkinter.Frame(window)
frame.pack()

# Criando Grid dos PESOS
pesos_frame = tkinter.LabelFrame(frame, text = "Insira os pesos iniciais")
pesos_frame.grid(row = 0, column = 0, padx = 20, pady = 20)

# Criando label para o peso1
peso1_label = tkinter.Label(pesos_frame, text= "W1:")
peso1_label.grid(row = 0, column = 0)
# Criando entrada para o peso1
peso1_entrada = tkinter.Entry(pesos_frame)
peso1_entrada.grid(row = 0, column = 1)

# Criando label para o peso2
peso2_label = tkinter.Label(pesos_frame, text= "W2:")
peso2_label.grid(row = 1, column = 0)
# Criando entrada para o peso2
peso2_entrada = tkinter.Entry(pesos_frame)
peso2_entrada.grid(row = 1, column = 1)

# Cirando um padding para todos os conteudos dentro do frame pesos_frame
for widget in pesos_frame.winfo_children():
    widget.grid_configure(padx = 5, pady = 5)

#-------------------------------------------------------------------------

# Criando Grid para o BIAS
bias_frame = tkinter.LabelFrame(frame, text = "Bias")
bias_frame.grid(row = 0, column = 1, padx = 20, pady = 20)

# Criando label para o X0
x0_label = tkinter.Label(bias_frame, text= "X0:")
x0_label.grid(row = 0, column = 0)
# Criando entrada para o X0
x0_entrada = tkinter.Entry(bias_frame)
x0_entrada.grid(row = 0, column = 1)

# Criando label para o peso0
peso0_label = tkinter.Label(bias_frame, text= "W0:")
peso0_label.grid(row = 1, column = 0)
# Criando entrada para o peso0
peso0_entrada = tkinter.Entry(bias_frame)
peso0_entrada.grid(row = 1, column = 1)

# Cirando um padding para todos os conteudos dentro do frame bias_frame
for widget in bias_frame.winfo_children():
    widget.grid_configure(padx = 5, pady = 5)

#-------------------------------------------------------------------------

# Criando Grid para o TREINO DOS NEURONIOS
treinoNeuronio_frame = tkinter.LabelFrame(frame, text = "Treino de Neurônios")
treinoNeuronio_frame.grid(row = 0, column = 2, padx = 20, pady = 20)

# Criando label para a taxa de aprendizagem
taxaAprendizagem_label = tkinter.Label(treinoNeuronio_frame, text= "Taxa de aprendizagem: ")
taxaAprendizagem_label.grid(row = 0, column = 0)
# Criando entrada para a taxa de aprendizagem
taxaAprendizagem_entrada = tkinter.Entry(treinoNeuronio_frame)
taxaAprendizagem_entrada.grid(row = 0, column = 1)

# Criando label para o numero max de treinos
numMaxTreinos_label = tkinter.Label(treinoNeuronio_frame, text= "Nº Máximo de treinos: ")
numMaxTreinos_label.grid(row = 1, column = 0)
# Criando entrada para o numero max de treinos
numMaxTreinos_entrada = tkinter.Entry(treinoNeuronio_frame)
numMaxTreinos_entrada.grid(row = 1, column = 1)

# Cirando um padding para todos os conteudos dentro do frame treinoNeuronio_frame
for widget in treinoNeuronio_frame.winfo_children():
    widget.grid_configure(padx = 5, pady = 5)

#-------------------------------------------------------------------------

# Criando Grid para os CASOS
casos_frame = tkinter.LabelFrame(frame, text = "Casos")
casos_frame.grid(row = 1, column = 0, padx = 20, pady = 20)

# Criando label para o X1
x1_label = tkinter.Label(casos_frame, text= "X1:")
x1_label.grid(row = 0, column = 0)
# Criando entrada para o X1
x1_entrada = tkinter.Entry(casos_frame)
x1_entrada.grid(row = 0, column = 1)

# Criando label para o X2
x2_label = tkinter.Label(casos_frame, text= "X2:")
x2_label.grid(row = 0, column = 2)
# Criando entrada para o X2
x2_entrada = tkinter.Entry(casos_frame)
x2_entrada.grid(row = 0, column = 3)

# Cirando um padding para todos os conteudos dentro do frame casos_frame
for widget in casos_frame.winfo_children():
    widget.grid_configure(padx = 5, pady = 5)

button = tkinter.Button(casos_frame, text = "Salvar")
button.grid(row = 0, column = 4)


# Criando uma comboBox
#title = tkinter.Label(pesos_frame, text = "Title")
#title_combobox = ttk.Combobox(pesos_frame, values=["alsos", "sda"])
#title.grid(row = 0, column = 2)
#title_combobox.grid(row = 1, column = 2)

# Criando uma spinBox
#age_label = tkinter.Label(pesos_frame, text = "Age")
#age_spinbox = tkinter.Spinbox(pesos_frame, from_ = 18, to = 100) # Cria uma delimentação para valores numericos na entrada
#age_label.grid(row = 0, column = 2)
#age_spinbox.grid(row = 1, column = 2)



# Loop para a GUI rodar até que seja fechada
window.mainloop()