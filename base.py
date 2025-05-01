import tkinter as tk
import subprocess
import time
from datetime import datetime
from tkinter import Label, Button, PhotoImage

# Función para actualizar el reloj en tiempo real
def update_clock():
    now = datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=now)
    root.after(1000, update_clock)

# Función para abrir la shell
#def open_shell():
    #subprocess.Popen(["x-terminal-emulator"])

def open_tetris():
    subprocess.Popen(["xterm", "-e", "tetris"])

def open_snake():
    subprocess.Popen(["xterm", "-e", "nsnake"])
    
def open_personalizar():
    pass

# Crear la ventana principal
root = tk.Tk()
root.title("NBA DESKTOP")
root.geometry("800x600")
root.configure(bg="skyblue")

# Etiqueta para el reloj
clock_label = Label(root, font=("Arial", 20), bg="skyblue")
clock_label.place(x=650, y=20)
update_clock()

# imagenes
img_shell = PhotoImage(file='casademont.png')
img_snake = PhotoImage(file='snake.png')
img_tetris = PhotoImage(file='tetris.png')
img_personalizar = PhotoImage(file='icono.png')

# Botón para abrir la Shell
#shell_button = Button(root, text="Abrir Shell", command=open_shell, font=("Arial", 12))
#shell_button.place(x=50, y=80)

# Botón para abrir la Snake
snake_button = Button(root, text="Snake",image=img_snake, compound='top', command=open_snake, font=("Arial", 12))
snake_button.place(x=50, y=80)

# Botón para abrir la Tetris
tetris_button = Button(root, text="Tetris",image=img_tetris, compound='top', command=open_tetris, font=("Arial", 12))
tetris_button.place(x=150, y=80)

# Botón para abrir la Personalizacion del fondo
fondo_button = Button(root, text="Personalizar fondo", image=img_personalizar, compound='top', command=open_personalizar, font=("Arial", 12))
fondo_button.place(x=250, y=80)
# Ejecutar la aplicación
root.mainloop()