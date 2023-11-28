#importando a biblioteca tkinder
from tkinter import *
from tkinter import ttk

#cores
cor1 = "#1e1f1e" #preto
cor2 = "#feffff" #branco
cor3 = "#38576b" #Azul
cor4 = "#ECEFF1" #Cinza
cor5 = "#FFAB40" #Laranja


janela = Tk()
janela.title("Calculadora")
janela.geometry("400x600")
janela.config(bg=cor1)

#criando frames/telas
frame_tela = Frame(janela,width=600, height=100, bg=cor2)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela,width=600, height=650,bg=cor1)
frame_corpo.grid(row=1, column=0)

#variavel todos os valores
todos_valores = ''


#criando funcao
def entrar_valores(event):

    global todos_valores

    todos_valores += str(event )

    #passando valor para a tela
    valor_texto.set(todos_valores)

#funcao para calucular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

#funcao para limpar a tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")  

    
    

#criando label(rótulo)
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable = valor_texto, width=22, height=3, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 21 bold'))
app_label.place(x=0,y=0)

#criando botoes

b1 = Button(frame_corpo,command=limpar_tela, text="C", width=26, height=5, bg=cor4, relief=RAISED)
b1.place(x=12, y=5)

b2 = Button(frame_corpo, command= lambda: entrar_valores('%'), text="%", width=12, height=5, bg=cor4)
b2.place(x=205, y=5)

b3 = Button(frame_corpo, command= lambda: entrar_valores('/'),text="/", width=12, height=5, bg=cor5, fg=cor2)
b3.place(x=300, y=5)

b4 = Button(frame_corpo, command= lambda: entrar_valores('7'),text="7", width=12, height=5, bg=cor4)
b4.place(x=15, y=95)

b5 = Button(frame_corpo, command= lambda: entrar_valores('8'),text="8", width=12, height=5, bg=cor4)
b5.place(x=110, y=95)

b6 = Button(frame_corpo, command= lambda: entrar_valores('9'),text="9", width=12, height=5, bg=cor4, fg=cor1)
b6.place(x=205, y=95)

b7 = Button(frame_corpo, command= lambda: entrar_valores('*'),text="X", width=12, height=5, bg=cor5, fg=cor2)
b7.place(x=300, y=95)

b8 = Button(frame_corpo, command= lambda: entrar_valores('4'),text="4", width=12, height=5, bg=cor4)
b8.place(x=15, y=185)

b9 = Button(frame_corpo, command= lambda: entrar_valores('5'),text="5", width=12, height=5, bg=cor4)
b9.place(x=110, y=185)

b10 = Button(frame_corpo, command= lambda: entrar_valores('6'),text="6", width=12, height=5, bg=cor4, fg=cor1)
b10.place(x=205, y=185)

b11= Button(frame_corpo, command= lambda: entrar_valores('-'),text="-", width=12, height=5, bg=cor5, fg=cor2)
b11.place(x=300, y=185)

b12 = Button(frame_corpo, command= lambda: entrar_valores('1'),text="1", width=12, height=5, bg=cor4)
b12.place(x=15, y=275)

b13 = Button(frame_corpo, command= lambda: entrar_valores('2'),text="2", width=12, height=5, bg=cor4)
b13.place(x=110, y=275)

b14= Button(frame_corpo, command= lambda: entrar_valores('3'),text="3", width=12, height=5, bg=cor4, fg=cor1)
b14.place(x=205, y=275)

b15 = Button(frame_corpo, command= lambda: entrar_valores('+'),text="+", width=12, height=5, bg=cor5, fg=cor2)
b15.place(x=300, y=275)

b16 = Button(frame_corpo, command= lambda: entrar_valores('0'),text="0", width=26, height=5, bg=cor4, relief=RAISED)
b16.place(x=12, y=365)

b17= Button(frame_corpo, command= lambda: entrar_valores('.'),text=".", width=12, height=5, bg=cor4, fg=cor1)
b17.place(x=205, y=365)

b15 = Button(frame_corpo, command= calcular,text="=", width=12, height=5, bg=cor5, fg=cor2)
b15.place(x=300, y=365)

janela.mainloop()