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
janela.geometry("480x725") #largura x comprimento da janela
janela.config(bg=preto)

frame_tela = Frame(janela, width=480, height=80, bg=azul) #subdivisão da tela da interface = parte superior
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=480, height=550) #subdivisão da corpo da interface
frame_corpo.grid(row=1, column=0)

#botoes

#primeira linha
b1 = Button(frame_corpo, text="C", width=19, height=4, font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=2)
b2 = Button(frame_corpo, text="%", width=9, height=4, font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=240, y=2)
b3 = Button(frame_corpo, text="/", width=9, height=4, font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE, bg=laranja, fg=branco)
b3.place(x=360, y=2)

#segunda linha

b4 = Button(frame_corpo, text="7", width=9, height=4, font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=117)
b5 = Button(frame_corpo, text="8", width=9, height=4, font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=120, y=117)
b6 = Button(frame_corpo, text="9", width=9, height=4, font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=240, y=117)
b7 = Button(frame_corpo, text="*", width=9, height=4, font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE, bg=laranja, fg=branco)
b7.place(x=360, y=117)

#terceira linha

b8 = Button(frame_corpo, text="4", width=9, height=4, font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=217)
b9 = Button(frame_corpo, text="5", width=9, height=4, font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=120, y=217)
b10 = Button(frame_corpo, text="6", width=9, height=4, font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=240, y=217)
b11 = Button(frame_corpo, text="-", width=9, height=4, font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE, bg=laranja, fg=branco)
b11.place(x=360, y=217)

#quarta linha

b12 = Button(frame_corpo, text="1", width=9, height=4, font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=317)
b13 = Button(frame_corpo, text="2", width=9, height=4, font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=120, y=317)
b14 = Button(frame_corpo, text="3", width=9, height=4, font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=240, y=317)
b15 = Button(frame_corpo, text="+", width=9, height=4, font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE, bg=laranja, fg=branco)
b15.place(x=360, y=317)

b1 = Button(frame_corpo, text="0", width=19, height=4, font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=432)
b2 = Button(frame_corpo, text=".", width=9, height=4, font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=240, y=432)
b3 = Button(frame_corpo, text="=", width=9, height=4, font=('Ivy 15 bold'), relief=RAISED, overrelief=RIDGE, bg=laranja, fg=branco)
b3.place(x=360, y=432)

janela.mainloop()