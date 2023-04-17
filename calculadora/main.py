from tkinter import *
from tkinter import ttk

#cores
preto = "#3b3b3b" 
branco = "#feffff"
azul = "#0f3675"
cinza = "#ECEFF1"
laranja = "#FFAB40"

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310") #largura x comprimento da janela
janela.config(bg=preto)

frame_tela = Frame(janela, width=235, height=50, bg=azul, pady=0, padx=0, relief="flat") #subdivisão da tela da interface = parte superior
frame_tela.grid(row=0, column=0, sticky=NW)

frame_corpo = Frame(janela, width=235, height=268) #subdivisão da corpo da interface
frame_corpo.grid(row=1, column=0)

#função para receber os valores digitados e concatenar

valor_texto = StringVar()
evento = ''

def click(event):

    global evento
    evento = evento + str(event)
    # resultado = eval(evento)
    valor_texto.set(evento) 

#calculos

def calc():
    global evento #tornar essa variável global nesta função, fará com que essa alteração passe para todas as outras funções/locais do código
    resultado = eval(evento) #A função Eval avalia o expressão de cadeia de caracteres e retorna seu valor. Por exemplo, Eval("1 + 1") retorna 2.
    valor_texto.set(resultado)

#limpar tela

def limpar_tela():
    global evento #tornar essa variável global nesta função, fará com que essa alteração passe para todas as outras funções/locais do código
    evento = ''
    valor_texto.set('')

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT,font=('Ivy 18'), bg=preto, fg=branco )
app_label.place(x=0,y=0)

#botoes

#primeira linha
b1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(frame_corpo, command = lambda: click('%'), text="%", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=118, y=0)
b3 = Button(frame_corpo, command = lambda: click('/'), text="/", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, bg=laranja, fg=branco)
b3.place(x=177, y=0)

#segunda linha

b4 = Button(frame_corpo, command = lambda: click('7'), text="7", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=52)
b5 = Button(frame_corpo, command = lambda: click('8'), text="8", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=59, y=52)
b6 = Button(frame_corpo, command = lambda: click('9'), text="9", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=118, y=52)
b7 = Button(frame_corpo, command = lambda: click('*'), text="*", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, bg=laranja, fg=branco)
b7.place(x=177, y=52)

#terceira linha

b8 = Button(frame_corpo, command = lambda: click('4'), text="4", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=104)
b9 = Button(frame_corpo, command = lambda: click('5'), text="5", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=59, y=104)
b10 = Button(frame_corpo, command = lambda: click('6'), text="6", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=118, y=104)
b11 = Button(frame_corpo, command = lambda: click('-'), text="-", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, bg=laranja, fg=branco)
b11.place(x=177, y=104)

#quarta linha

b12 = Button(frame_corpo, command = lambda: click('1'), text="1", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=156)
b13 = Button(frame_corpo, command = lambda: click('2'), text="2", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=59, y=156)
b14 = Button(frame_corpo, command = lambda: click('3'), text="3", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=118, y=156)
b15 = Button(frame_corpo, command = lambda: click('+'), text="+", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, bg=laranja, fg=branco)
b15.place(x=177, y=156)

#quinta linha

b16 = Button(frame_corpo, command = lambda: click('0'), text="0", width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=208)
b17 = Button(frame_corpo, command = lambda: click('.'), text=".", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=118, y=208)
b18 = Button(frame_corpo, command = calc, text="=", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, bg=laranja, fg=branco)
b18.place(x=177, y=208)

janela.mainloop() #executa a visualização gráfica