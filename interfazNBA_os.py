import tkinter as tk
import subprocess
import time
import platform
from datetime import datetime
from tkinter import Label, Button, PhotoImage

# Función para actualizar el reloj en tiempo real
def update_clock():
    now = datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=now)
    root.after(1000, update_clock)

# Función para abrir la Shell
def open_shell():
    system = platform.system()
    if system == "Linux":
        # Abre xterm en lugar de gnome-terminal
        subprocess.Popen(["xterm", "-e", "bash /home/maikol3/NBA_os.sh" ])
    elif system == "Windows":
        subprocess.Popen(["cmd.exe"])
    else:
        print("Sistema no compatible")


def open_tetris():
    subprocess.Popen(["xterm", "-e", "bastet"])

def open_snake():
    subprocess.Popen(["xterm", "-e", "nsnake"])
    


# Crear la ventana principal
root = tk.Tk()
root.title("NBA DESKTOP")
root.geometry("800x600")
root.configure(bg="skyblue")

# imagen del fondo
fondo_img = PhotoImage(file="chicago bulls.png") 
bg_label = Label(root, image=fondo_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Etiqueta para el reloj
clock_label = Label(root, font=("Arial", 20), bg="darkred")
clock_label.place(x=650, y=20)
update_clock()

# imagenes
img_shell = PhotoImage(file='casademont.png')
img_snake = PhotoImage(file='snake.png')
img_tetris = PhotoImage(file='tetris.png')


# Botón para abrir la Shell
shell_button = Button(root, text="Shell", image=img_shell, compound='top', command=open_shell, font=("Arial", 12))
shell_button.place(x=450, y=80)

# Botón para abrir la Snake
snake_button = Button(root, text="Snake",image=img_snake, compound='top', command=open_snake, font=("Arial", 12))
snake_button.place(x=50, y=80)

# Botón para abrir la Tetris
tetris_button = Button(root, text="Tetris",image=img_tetris, compound='top', command=open_tetris, font=("Arial", 12))
tetris_button.place(x=250, y=80)

# Ejecutar la aplicación
root.mainloop()