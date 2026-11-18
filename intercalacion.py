import tkinter as tk
from tkinter import messagebox

def intercalar(lista1, lista2):
    resultado = []
    i = j = 0
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado

def ejecutar_intercalacion():
    try:
        # Convertir cadenas separadas por coma a listas de enteros
        l1 = [int(x.strip()) for x in entry_lista1.get().split(",") if x.strip()]
        l2 = [int(x.strip()) for x in entry_lista2.get().split(",") if x.strip()]
        
        if not l1 or not l2:
            messagebox.showwarning("Advertencia", "Por favor ingresa números en ambas listas.")
            return

        # Asegurar que las listas de entrada estén ordenadas para la intercalación
        l1.sort()
        l2.sort()
        
        res = intercalar(l1, l2)
        lbl_resultado.config(
            text=f"Lista 1 ordenada: {l1}\n"
                 f"Lista 2 ordenada: {l2}\n\n"
                 f"Resultado Intercalado:\n{res}",
            fg="#1b5e20"
        )
    except ValueError:
        messagebox.showerror("Error de formato", "Ingresa únicamente números enteros separados por comas (ej. 1, 3, 5).")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Método de Intercalación")
ventana.geometry("450x340")
ventana.resizable(False, False)
ventana.config(padx=20, pady=20)

tk.Label(ventana, text="Ordenamiento por Intercalación", font=("Arial", 14, "bold")).pack(pady=(0, 15))

tk.Label(ventana, text="Lista 1 (números separados por comas):", font=("Arial", 10)).pack(anchor="w")
entry_lista1 = tk.Entry(ventana, width=50, font=("Arial", 10))
entry_lista1.insert(0, "1, 3, 5, 7")
entry_lista1.pack(pady=(2, 10))

tk.Label(ventana, text="Lista 2 (números separados por comas):", font=("Arial", 10)).pack(anchor="w")
entry_lista2 = tk.Entry(ventana, width=50, font=("Arial", 10))
entry_lista2.insert(0, "2, 4, 6, 8, 10")
entry_lista2.pack(pady=(2, 15))

btn_ordenar = tk.Button(ventana, text="Intercalar Listas", command=ejecutar_intercalacion, bg="#1976d2", fg="white", font=("Arial", 10, "bold"), padx=15, pady=5)
btn_ordenar.pack()

lbl_resultado = tk.Label(ventana, text="", font=("Arial", 10, "bold"), justify="left", wraplength=400)
lbl_resultado.pack(pady=15)

ventana.mainloop()