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
    print("Line Plot")

    # NOTA: aproveche los ejemplos "multi_line_plot" de clase

    # Se desea graficar varias funciones en un mismmo gráfico (axe)

    # Las funciones que se desean implementar y graficar son:
    # y1 = x**2
    # y2 = x**3

    # Su implementación ya está disponible, es la siguiente:
    x = list(np.linspace(-4, 4, 20))

    y1 = []
    for i in x:
        y1.append(i**2)

    y2 = []
    for i in x:
        y2.append(i**3)

    # Alumno: Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "ax"

    # Se debe colocar en la leyenda la función que representa
    # cada función

    # Cada función dibujarla con un color distinto
    # a su elección

    # Crear acá su gráfico

    
    fig = plt.figure()
    ax = fig.add_subplot()
    fig.suptitle('Ejercicio 2', fontsize=18)
    
    #Grafico
    ax.plot(x, y1, label='y1 = x**2', c='#395B64' )
    ax.plot(x, y2, label='y2 = x**3', c='#11468F' )
    
    #Personalizacion
    ax.set_title("Line plot", fontsize=14)
    ax.set_ylabel("Eje Y")
    ax.set_xlabel("Eje X")
    ax.set_facecolor('#F5F2E7')
    ax.legend()
    ax.grid()

    #Muestro
    
    plt.show()
    
    print("terminamos")
