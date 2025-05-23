# Análisis de satisfacción de clientes con Python
 # Autor: [Tu nombre]
 # Fecha: [Año]
 
 import pandas as pd
 import matplotlib.pyplot as plt
 
 # Creamos un pequeño dataset simulado
 data = {
     'Cliente': ['A', 'B', 'C', 'D', 'E'],
     'Satisfaccion': [7, 5, 6, 8, 4]
 }
 
 df = pd.DataFrame(data)
 
 # Mostramos estadísticas básicas
 print("Media de satisfacción:", df['Satisfaccion'].mean())
 print("Desviación estándar:", df['Satisfaccion'].std())
 print("\nTabla descriptiva completa:")
 print(df.describe())
 
 # Gráfico de barras
 plt.figure(figsize=(6,4))
 plt.bar(df['Cliente'], df['Satisfaccion'], color='skyblue')
 plt.title('Nivel de satisfacción por cliente')
 plt.xlabel('Cliente')
 plt.ylabel('Satisfacción')
 plt.ylim(0,10)
 plt.grid(axis='y', linestyle='--', alpha=0.7)
 plt.tight_layout()
 
 # Guardamos el gráfico como imagen
 plt.savefig('grafico_satisfaccion.png')
 plt.show()
