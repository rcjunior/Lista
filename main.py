#!/usr/bin/python3

__author__ = 'R. C. Junior'

from tkinter import *

class Janela:
    def __init__(self, instancia_tk):

        # Titulo
        self.root = root
        self.root.title("Páginação")

        #Frame titulo
        self.lbl_space0 = Label(self.root, text=" ")
        self.lbl_space0.grid(row=1, column=1, columnspan=9)

        self.lbl_title = Label(self.root, text="Paginação", font=('Verdana', '15', 'bold'))
        self.lbl_title.grid(row=2, column=1, columnspan=9, sticky=NSEW)

        #Frame primario

        self.lbl_space1 = Label(self.root, text=" ", font=("verdana", 15))
        self.lbl_space1.grid(row=3, column=1, columnspan=9)

        self.lbl_square = Label(self.root, text="Quadrado: ")
        self.lbl_square.grid(row=3, column=2)

        self.ent_square = Entry(self.root)
        self.ent_square.grid(row=3, column=4)

        self.lbl_algo = Label(self.root, text="Algoritmo: ")
        self.lbl_algo.grid(row=3, column=6)

        optionList = ('FIFO', 'LIFO', 'LRU', 'Otimo')
        self.var = StringVar()
        self.var.set(optionList[0])
        self.opt_algo = OptionMenu(self.root, self.var, *optionList)
        self.opt_algo.grid(row=3, column=7, sticky=NSEW)

        #Frame secundario

        self.lbl_number = Label(self.root, text="Número: ")
        self.lbl_number.grid(row=4, column=2)

        self.ent_number = Entry(self.root)
        self.ent_number.grid(row=4, column=4)

        self.btn_process = Button(self.root, text="Processar", bg="blue", fg="skyblue", font=('verdana', 10, 'bold'))
        self.btn_process.grid(row=4, column=6, columnspan=2, sticky=NSEW)

        #square's frame

        self.lbl_space2 = Label(self.root, text=" ")
        self.lbl_space2.grid(row=5, column=1, columnspan=9)

        rows = []
        for i in range(6,11): #aqui é onde deve ser inserido o valor inserido no square
            cols = []
            for j in range(2,9):
                e = Entry(relief=RIDGE)
                e.grid(row=i, column=j, sticky=NSEW)
                e.insert(END, '%d.%d' % (i, j))
                cols.append(e)
            rows.append(cols)

        self.lbl_spacevert0 = Label(self.root, text=" ")
        self.lbl_spacevert0.grid(row=6, column=1, rowspan=i)

        self.lbl_spacevert1 = Label(self.root, text=" ")
        self.lbl_spacevert1.grid(row=6, column=9, rowspan=i)

        #buttons

        self.lbl_space3 = Label(self.root, text=" ")
        self.lbl_space3.grid(row=i+5, column=1, columnspan=9)

        self.btn_clear = Button(self.root, text="Limpar", font=('Verdana', 10, 'bold'), bg="yellow")
        self.btn_clear.grid(row=i+6, column=3, columnspan=2, sticky=NSEW)

        self.btn_exit = Button(self.root, text="Sair", font=('Verdana', 10, 'bold'), bg="red", fg="pink")
        self.btn_exit.grid(row=i+6, column=6, columnspan=2, sticky=NSEW)

        self.lbl_space3 = Label(self.root, text=" ")
        self.lbl_space3.grid(row=i+7, column=1, columnspan=9)

root = Tk()
Janela(root)
root.mainloop()