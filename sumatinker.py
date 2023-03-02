from tkinter import *


def sumar():
    try:
        lb_result["text"] = "Resultado: " + str(int(lb_juan.get()) + int(lb_andres.get()))
    except:
        lb_result["text"] = "Resultado: error, no se pudo convertir a entero esta cadena"


wnd = Tk()
wnd.geometry("400x400")
wnd.title("emilio")
btn_sum = Button(wnd, text="Sumar", command=sumar)
lb_result = Label(wnd, text="Resultado:")
btn_sum.place(x=50, y=127)
lb_result.place(x=50, y=160)
lb_a = Label(wnd, text="a:")
lb_a.place(x=45, y=50)
lb_b = Label(wnd, text="b:")
lb_b.place(x=45, y=100)
lb_andres = Entry(wnd)
lb_andres.place(x=80, y=100)
lb_juan = Entry(wnd)
lb_juan.place(x=80, y=50)
wnd.mainloop()