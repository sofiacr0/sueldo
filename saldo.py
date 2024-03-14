import tkinter as tk
from tkinter import messagebox

def calcular_saldo_neto():
    try:
        salario_bruto = float(entry_salario_bruto.get())
        deducciones = float(entry_deducciones.get())
        impuestos = float(entry_impuestos.get())
        
        saldo_neto = salario_bruto - deducciones - impuestos
        
        label_resultado.config(text=f"Saldo Neto: ${saldo_neto:.2f}", fg="green")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

# Configuración de la ventana
root = tk.Tk()
root.title("Calculadora de Saldo Neto")
root.geometry("600x400")  # Tamaño de la ventana

# Color de fondo
root.configure(bg="white")

# Etiqueta y campo de entrada para el salario bruto
label_salario_bruto = tk.Label(root, text="Salario Bruto:", bg="white")
label_salario_bruto.grid(row=0, column=0, padx=10, pady=5)
entry_salario_bruto = tk.Entry(root)
entry_salario_bruto.grid(row=0, column=1, padx=10, pady=5)

# Etiqueta y campo de entrada para las deducciones
label_deducciones = tk.Label(root, text="Deducciones:", bg="white")
label_deducciones.grid(row=1, column=0, padx=10, pady=5)
entry_deducciones = tk.Entry(root)
entry_deducciones.grid(row=1, column=1, padx=10, pady=5)

# Etiqueta y campo de entrada para los impuestos
label_impuestos = tk.Label(root, text="Impuestos:", bg="white")
label_impuestos.grid(row=2, column=0, padx=10, pady=5)
entry_impuestos = tk.Entry(root)
entry_impuestos.grid(row=2, column=1, padx=10, pady=5)

# Botón para calcular el saldo neto
btn_calcular = tk.Button(root, text="Calcular Saldo Neto", command=calcular_saldo_neto, bg="white", fg="black")
btn_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(root, text="", bg="white")
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
