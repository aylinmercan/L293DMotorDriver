

import serial
import time
import tkinter as tk
 
window = tk.Tk()
window.configure(background="gray")
window.geometry("330x80")
window.title("MOTOR CTRL - PYTHON GUI")
 
megaBoard = serial.Serial('COM5', 9600)

def motor_control():
    print(">>> MOTOR CTRL PROGRAM <<<\n")



    def forward():
        print("CTRL -> FORWARD ")
        megaBoard.write(b'F')
 
    def reverse():
        print("CTRL -> REVERSE")
        megaBoard.write(b'R')
 
    def quit():
        print("\n** END OF PROGRAM **")
        megaBoard.write(b'Q')
        megaBoard.close()
        window.destroy()
 
    b1 = tk.Button(window, text="FORWARD", command=forward, bg="forest green", fg="gray7", font=("Comic Sans MS", 15))
 
    b2 = tk.Button(window, text="REVERSE", command=reverse, bg="firebrick2", fg="ghost white", font=("Comic Sans MS", 15))
 
    b3 = tk.Button(window, text="EXIT", command=quit, bg="gold", fg="gray7", font=("Comic Sans MS", 15))
 
    b1.grid(row=1, column=0, padx=5, pady=10)
    b2.grid(row=1, column=1, padx=5, pady=10)
    b3.grid(row=1, column=2, padx=5, pady=10)
 
    window.mainloop()
 
time.sleep(2)
motor_control()
