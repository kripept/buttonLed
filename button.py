import tkinter as tk
#from pyfirmata import Arduino 

def ledON():
    board.digital[3].write(1)
def ledOFF():
    board.digital[3].write(0)

#board = Arduino("COM3")

win = tk.Tk()
# Инициализация окна
win.title("Dimmer LED")
win.minsize(200, 60)
# Создаем надписи label ну тип текст
label = tk.Label(win, text="Нажмите, чтодбы вкл/выкл")
label.grid (column =1, row = 1)
#кнопки вкл выкл делаем
ONbtn = tk.Button(win, bd=4, text="LED ВКЛ", command=ledON)
ONbtn.grid (column=1, row=2)
OFFbtn = tk.Button(win, bd=4, text="LED выкл", command=ledOFF)
OFFbtn.grid (column=2, row=2)

win.mainloop()