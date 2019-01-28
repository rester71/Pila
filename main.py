from Pila import Pila
import tkinter as tk
from tkinter import *
from random import randint


class UI(object):
    tam = 10
    # Posicion del rectangulo
    x0 = 120
    y0 = 200
    x1 = 220
    y1 = 220

    pila = None
    figuras = None

    def __init__(self, root):
        self.root = root
        self.entry = tk.Entry(root)
        # Declarar PILA
        self.pila = Pila(self.tam)
        self.canvas = tk.Canvas(
            root,
            width=300,
            height=220,
            background='white'
        )
        self.canvas.grid(row=0, column=1, sticky='n')

        frame = tk.Frame(self.root)
        frame.grid(row=0, column=0, sticky='n')

        texto = tk.Label(frame, text="Programa PILAA").grid(
            row=0, column=2, sticky=N + E, padx=50, columnspan=3
        )
        buttonPush = tk.Button(
            frame, text="PUSH",
            command=self.push_command
        ).grid(
            row=1, column=2, sticky=W + E,
            padx=50, columnspan=3, pady=20
        )
        buttonPOP = tk.Button(
            frame,
            text="POP",
            command=self.pop_command
            ).grid(
            row=2, column=2, sticky=W + E,
            padx=50, columnspan=3, pady=20
        )

    def push_command(self):
        if self.pila.llena():
            # ALERTA
            return
        else:
            rand1 = randint(10, 99)
            rand2 = randint(10, 99)
            self.pila.push(self.canvas.create_rectangle(
                self.x0, self.y0, self.x1, self.y1,
                fill="#" + str(rand1) + "ff" + str(rand2)
            ))
            self.y0 -= 20
            self.y1 -= 20

    def pop_command(self):
        if self.pila.vacia():
            # ALERTA
            return
        else:
            figura = self.pila.pop()
            self.canvas.delete(figura)
            self.y0 += 20
            self.y1 += 20


if __name__ == '__main__':
    root = tk.Tk()
    interfaz = UI(root)
    root.mainloop()
