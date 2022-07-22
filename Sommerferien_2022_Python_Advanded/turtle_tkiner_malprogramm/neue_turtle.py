import turtle
from tkinter import *

fenster = Tk()

fenster.title("Kreisprogramm")

canvas = Canvas(master=fenster, width=400, height=400)
canvas.pack()



def main():
    canvas.bind_all("<KeyPress-w>",w_testfunktion)
    canvas.bind_all("<KeyPress-k>",k_testfunktion)

    fenster.mainloop()

    
def w_testfunktion(event):
    print("w taste")

    
def k_testfunktion(event):
    print("k taste")

main()
