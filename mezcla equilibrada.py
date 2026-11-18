import tkinter as tk
from tkinter import messagebox

def _particionar_tramos(lista):
    if not lista:
        return []
    tramos = [[lista[0]]]
    for x in lista[1:]:
        if x >= tramos[-1][-1]:
            tramos[-1].append(x)
        else:
            tramos.append([x])
    return tramos

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

def mezcla_equilibrada(lista):
    if len(lista) <= 1:
        return lista, [lista]
    
    tramos_iniciales = _particionar_tramos(lista)
    tramos = list(tramos_iniciales)
    
    while len(tramos) > 1:
        nuevos_tramos = []
        for i in range(0, len(tramos), 2):
            if i + 1 < len(tramos):
                nuevos_tramos.append(_fusionar(tramos[i], tramos[i+1]))
            else:
                nuevos_tramos.append(tramos[i])
        tramos = nuevos_tramos

    return tramos[0], tramos_iniciales

def ejecutar_mezcla_equilibrada():
    try:
        datos = [int(x.strip()) for x in entry_datos.get().split(",") if x.strip()]
        if not datos:
            messagebox.showwarning("Advertencia", "Ingresa al menos un número.")
            return
            
        ordenados, tramos = mezcla_equilibrada(datos)
        lbl_resultado.config(
            text=f"Tramos naturales detectados ({len(tramos)}):\n{tramos}\n\n"
                 f"Resultado final ordenado:\n{ordenados}",
            fg="#4a148c"
        )
    except ValueError:
        messagebox.showerror("Error de formato", "Ingresa únicamente números enteros separados por comas.")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Método de Mezcla Equilibrada")
ventana.geometry("460x330")
ventana.resizable(False, False)
ventana.config(padx=20, pady=20)

tk.Label(ventana, text="Ordenamiento por Mezcla Equilibrada", font=("Arial", 14, "bold")).pack(pady=(0, 15))

tk.Label(ventana, text="Ingresa los números (separados por comas):", font=("Arial", 10)).pack(anchor="w")
entry_datos = tk.Entry(ventana, width=52, font=("Arial", 10))
entry_datos.insert(0, "12, 15, 18, 3, 9, 20, 1, 4, 7")
entry_datos.pack(pady=(5, 15))

btn_ejecutar = tk.Button(ventana, text="Detectar Tramos y Ordenar", command=ejecutar_mezcla_equilibrada, bg="#6a1b9a", fg="white", font=("Arial", 10, "bold"), padx=15, pady=5)
btn_ejecutar.pack()

lbl_resultado = tk.Label(ventana, text="", font=("Arial", 10, "bold"), justify="left", wraplength=410)
lbl_resultado.pack(pady=15)

ventana.mainloop()