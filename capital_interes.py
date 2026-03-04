# Programa en Python para ingresar un capital e imprimir en cuantos meses se duplica según un interés compuesto del 5%

# ibraries
import math

# input
print(" ██████╗ ██╗   ██╗███████╗    ████████╗ █████╗ ██╗         ██████╗ ███████╗██████╗  █████╗ ")
print("██╔═══██╗██║   ██║██╔════╝    ╚══██╔══╝██╔══██╗██║         ██╔══██╗██╔════╝██╔══██╗██╔══██╗")
print("██║   ██║██║   ██║█████╗         ██║   ███████║██║         ██████╔╝█████╗  ██████╔╝███████║")
print("██║▄▄ ██║██║   ██║██╔══╝         ██║   ██╔══██║██║         ██╔═══╝ ██╔══╝  ██╔═══╝ ██╔══██║")
print("╚██████╔╝╚██████╔╝███████╗       ██║   ██║  ██║███████╗    ██║     ███████╗██║     ██║  ██║")
print(" ╚══▀▀═╝  ╚═════╝ ╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚══════╝╚═╝     ╚═╝  ╚═╝")
print("")
print("      Capital duplicado en n meses      ")
print("")

c=int(input("digite el valor del capital que desee colocar para invertir: "))
d=2*c
n=0

# procssing

while(c<d):
    c=1.05*c
    n=n+1
    print(c)

# output
print("")
print("      RESULTADOS      ")
print("")
print("el capital se duplicará en: " +str(n) +str(" meses"))
print("")

print("███╗   ███╗██╗    ██████╗  ██████╗ ███╗   ███╗██████╗  ██████╗ ")
print("████╗ ████║██║    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔═══██╗")
print("██╔████╔██║██║    ██████╔╝██║   ██║██╔████╔██║██████╔╝██║   ██║")
print("██║╚██╔╝██║██║    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██║   ██║")
print("██║ ╚═╝ ██║██║    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝╚██████╔╝")
print("╚═╝     ╚═╝╚═╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝  ╚═════╝ ")