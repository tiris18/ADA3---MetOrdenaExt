import tkinter as tk
from tkinter import messagebox

def _fusionar(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def mezcla_directa(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = mezcla_directa(lista[:medio])
    derecha = mezcla_directa(lista[medio:])
    return _fusionar(izquierda, derecha)

def ejecutar_mezcla_directa():
    try:
        datos = [int(x.strip()) for x in entry_datos.get().split(",") if x.strip()]
        if not datos:
            messagebox.showwarning("Advertencia", "Ingresa al menos un número.")
            return
            
        ordenados = mezcla_directa(datos)
        lbl_resultado.config(
            text=f"Original ({len(datos)} elementos):\n{datos}\n\n"
                 f"Ordenado por Mezcla Directa:\n{ordenados}",
            fg="#0d47a1"
        )
    except ValueError:
        messagebox.showerror("Error de formato", "Ingresa únicamente números enteros separados por comas.")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Método de Mezcla Directa")
ventana.geometry("450x310")
ventana.resizable(False, False)
ventana.config(padx=20, pady=20)

tk.Label(ventana, text="Ordenamiento por Mezcla Directa", font=("Arial", 14, "bold")).pack(pady=(0, 15))

tk.Label(ventana, text="Ingresa los números desordenados (separados por comas):", font=("Arial", 10)).pack(anchor="w")
entry_datos = tk.Entry(ventana, width=50, font=("Arial", 10))
entry_datos.insert(0, "38, 27, 43, 3, 9, 82, 10")
entry_datos.pack(pady=(5, 15))

btn_ejecutar = tk.Button(ventana, text="Ordenar Lista", command=ejecutar_mezcla_directa, bg="#2e7d32", fg="white", font=("Arial", 10, "bold"), padx=15, pady=5)
btn_ejecutar.pack()

lbl_resultado = tk.Label(ventana, text="", font=("Arial", 10, "bold"), justify="left", wraplength=400)
lbl_resultado.pack(pady=15)

ventana.mainloop()