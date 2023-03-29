import tkinter as tk

def calcular_idade():
    idade = int(entrada_idade.get())
    resultado.config(text=f"Sua idade é: {idade} anos.")

janela = tk.Tk()
janela.geometry("350x175")

titulo = tk.Label(janela, text="Calculadora de idade", font=("Arial", 14))
titulo.pack(pady=10)

label_idade = tk.Label(janela, text="Qual é a sua idade?", font=("Arial", 9))
label_idade.pack()

entrada_idade = tk.Entry(janela, font=("Arial", 9))
entrada_idade.pack()

botao = tk.Button(janela, text="Calcular idade", font=("Arial", 9), command=calcular_idade)
botao.pack(pady=10)

resultado = tk.Label(janela, text="", font=("Arial", 9))
resultado.pack()

janela.mainloop()