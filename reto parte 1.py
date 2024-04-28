"""
Dados los coeficientes de la ecuación cuadrática a*x^2+b*x+c=0 ingresados por consola (a, b y c),
resolver en R (números reales) e imprimir por pantalla los valores de las soluciones x1 y x2.
Si no hay solución indicar que no hay con un texto.
Dada la ecuación de la parte 1, hallar las soluciones en C (números complejos).
Considerar que si el discriminante es < 0, las soluciones tendrán parte real y parte imaginaria
(*) Usar todo lo visto en las sesiones 01 y 02 (variables, print, condicionales)
"""

print("Para la siguiente ecuación cuadrática -> ax² + bx + c")

a = float(input("Ingresa 'a': "))
b = float(input("Ingresa 'b': "))
c = float(input("Ingresa 'c': "))

discriminante = b**2 - 4*c*a

if discriminante < 0:
    r = (-1)*b / (2*a)
    c = ((-1)*discriminante)**(1/2) / (2*a)
    print("La raíces son de natulareza compleja.")

    if c < 0:
        print("La raíz x₁ es ", r, " - ", (-1)*c, "i", sep="")
        print("La raíz x₂ es ", r, " - ", (-1)*c, "i", sep="")
    else:
        print("La raíz x₁ es ", r, " + ", c, "i", sep="")
        print("La raíz x₂ es ", r, " - ", c, "i", sep="")

else:
    x_1 = ((-1)*b + discriminante**(1/2)) / (2*a)

    if discriminante == 0:
        print("Las raíces son reales e iguales.")
        print("La raíz doble es", x_1)
        
    else:
        x_2 = ((-1)*b - discriminante**(1/2)) / (2*a)
        print("Las raíces son reales")
        print("La raíz x₁ es", x_1)
        print("La raíz x₂ es", x_2)
