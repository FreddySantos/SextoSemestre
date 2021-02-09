import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.canvas1 = tk.Canvas(self.ventana1, width=700, height=500, background="white")
        self.canvas1.grid(column=0, row=0)
        self.canvas1.create_line(0, 0, 100, 50, fill="black")
        self.canvas1.create_rectangle(150, 10, 250, 110, fill="black")
        self.canvas1.create_rectangle(150, 210, 250, 310, outline="black")

        self.canvas1.create_oval(300, 10, 400, 150, fill="green")
        self.canvas1.create_oval(300, 210, 400, 350, outline="green")

        self.canvas1.create_arc(420, 10, 550, 110, fill="red", start=180, extent=90)
        self.canvas1.create_arc(420, 210, 550, 310, outline="red", start=180, extent=90)

        self.ventana1.mainloop()


aplicacion1 = Aplicacion()
