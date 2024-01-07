import tkinter as tk
from tkinter import *







def Calculadora_Model():
# Paleta de cores
    cor1 = "#282829" # black/preta
    cor2 = "#feffff" # white/branca
    cor3 = "#38576b" # Blue/azul
    cor4 = "#ECEFF1" # Grey/cinza
    cor5 = "#FFAB40" # Orange/laranja

    # Interface
    janela = tk.Toplevel()
    janela.title("Calculadora")
    janela.geometry("239x318")
    janela.config(bg=cor1)
    icone = tk.PhotoImage(file='calculadora.png')
    janela.iconphoto(False, icone)
    janela.resizable(width=False, height=False)




    # Frames
    frame_tela = Frame(janela, width=240, height=58, bg=cor3)
    frame_tela.grid(row=0, column=0)

    frame_corpo = Frame(janela, width=240, height=260)
    frame_corpo.grid(row=1, column=0)


    global valor_texto
    valor_texto = StringVar()
    # label texto dos calculos
    app_label = Label(frame_tela, textvariable = valor_texto, width=13, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 20 bold'), bg=cor3, fg=cor2)
    app_label.place(x=0, y=0)


    global todos_valores
    todos_valores = ''

    # função calculadora

    def entrar_valores(event):
        global todos_valores
        todos_valores = todos_valores + str(event)

        valor_texto.set(todos_valores)


    # função para calcular

    def calcular():
        global todos_valores
        resultado = eval(todos_valores)
        valor_texto.set(str(resultado))


    # função limpa tela

    def limpar_tela():
        global todos_valores
        todos_valores = ''
        valor_texto.set('')


    # primeira fileira de botões
    b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_1.place(x=0, y=0)

    b_2 = Button(frame_corpo, command= lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_2.place(x=120.4, y=0)

    b_3 = Button(frame_corpo, command= lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_3.place(x=180, y=0)


    # segunda fileira de botões
    b_4 = Button(frame_corpo, command= lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_4.place(x=0, y=52)

    b_5 = Button(frame_corpo, command= lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_5.place(x=59.5, y=52)

    b_6 = Button(frame_corpo, command= lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_6.place(x=120.4, y=52)

    b_7 = Button(frame_corpo, command= lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_7.place(x=180, y=52)


    # terceira fileira de botões
    b_8 = Button(frame_corpo, command= lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_8.place(x=0, y=104)

    b_9 = Button(frame_corpo, command= lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_9.place(x=59.5, y=104)

    b_10 = Button(frame_corpo, command= lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_10.place(x=120.4, y=104)

    b_11 = Button(frame_corpo, command= lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_11.place(x=180, y=104)

    # quarta fileira de botões
    b_12 = Button(frame_corpo, command= lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_12.place(x=0, y=156)

    b_13 = Button(frame_corpo, command= lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_13.place(x=59.5, y=156)

    b_14 = Button(frame_corpo, command= lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_14.place(x=120.4, y=156)

    b_15 = Button(frame_corpo, command= lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_15.place(x=180, y=156)


    # quinta fileira de botões
    b_16 = Button(frame_corpo, command= lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_16.place(x=0, y=208)

    b_17 = Button(frame_corpo, command= lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_17.place(x=120.4, y=208)

    b_18 = Button(frame_corpo, command= calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_18.place(x=180, y=208)
    janela.mainloop()


root = tk.Tk()
root.title("Torquato Tech")

icone1 = tk.PhotoImage(file='MateusTor.png')
root.iconphoto(False, icone1)
root.resizable(width=False, height=False)
# Carregar a imagem da sua logo
image = tk.PhotoImage(file="TorquatoTech.png")  # Substitua pelo caminho correto da sua logo
# Redimensionar a imagem para 318x318
image = image.subsample(int(image.width() / 318))

# Criar um rótulo para exibir a imagem da logo
label = tk.Label(root, image=image)
label.pack()


# Criar um botão sobre a imagem
button = tk.Button(root, text="Calculadora", command=Calculadora_Model)
button.place(relx=0.95, rely=0.5, anchor=tk.E)
#root.after(5000, Calculadora_Model)
root.mainloop()


    

