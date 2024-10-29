from tkinter import ttk
import tkinter as tk
import keyboard

caps = False
caps_pressed = False  # Variable para controlar el estado de la tecla
root = tk.Tk()
root.withdraw()  # Oculta la ventana principal

def teclado(event):
    global caps, caps_pressed
    if event.name == 'caps lock':
        if event.event_type == 'down':  # Si la tecla es presionada
            if not caps_pressed:  # Solo si no se había procesado antes
                if caps:
                    Ventana(False)  # Llama a Ventana con estado False
                    caps = False
                else:
                    Ventana(True)   # Llama a Ventana con estado True
                    caps = True
                caps_pressed = True  # Marca que se ha procesado la pulsación
        elif event.event_type == 'up':  # Si la tecla es soltada
            caps_pressed = False  # Resetea el estado al soltar

def Ventana(status: bool):
    ventana = tk.Toplevel(root)  # Usa Toplevel para la ventana
    if status:
        ventana.title('Mayúsculas')
        image = tk.PhotoImage(file="mayus.png")
        label = ttk.Label(ventana, image=image)
        label.image = image  # Guarda la referencia a la imagen
    else:
        ventana.title('Minúsculas')
        image2 = tk.PhotoImage(file="minus.png")
        label = ttk.Label(ventana, image=image2)
        label.image = image2  # Guarda la referencia a la imagen

    label.pack()
    ventana.geometry("300x300")
    
    # Cierra la ventana después de 1 segundo
    ventana.after(1000, ventana.destroy)

# Registra el evento de teclado
keyboard.hook(teclado)

# Bucle principal de Tkinter
try:
    root.mainloop()
except KeyboardInterrupt:
    pass
finally:
    keyboard.unhook_all()  # Asegúrate de desactivar el hook del teclado
