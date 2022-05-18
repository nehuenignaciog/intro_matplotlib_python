# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Scatter Plot")

    # NOTA: aproveche los ejemplos "scatter_plot" de clase

    # Se desea graficar la función tanh para el siguiente
    # intervalor de valores de "X"
    x = np.arange(-np.pi, np.pi, 0.1)

    # Función y = tanh(x) --> tangente hiperbólica
    y = np.tanh(x)

    # Alumno: Graficar la función utilizando "scatter"
    # utilizando "x" e "y" ya disponible

    # Colocar la leyenda y el label con el nombre de la función

    # Elegir un marker a elección

    # Crear acá su gráfico


    fig = plt.figure()
    ax = fig.add_subplot()
    fig.suptitle('Ejercicio 3', fontsize=18)
    ax = fig.add_subplot()  
    
    #Grafico
    ax.scatter(x, y, label ="y = tanh(x)",c='#1A374D', marker='.')

    #Personalizacion
    ax.set_title("Tangente hiperbólica", fontsize=14)
    ax.set_ylabel("Eje Y")
    ax.set_xlabel("Eje X")
    ax.set_facecolor('#B1D0E0')
    ax.legend()
    ax.grid()
   
    #Muestro
    
    plt.show()

    print("terminamos")
