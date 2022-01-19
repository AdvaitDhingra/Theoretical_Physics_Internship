from typing import Type
import sympy as sp
from sympy import sympify

P0 = sp.Symbol("P0")
P1 = sp.Symbol("P1")
P2 = sp.Symbol("P2")

z = float(eval("1/18")) # Unser Wert von z (ind er Aufgabe gegeben)

Theta = sp.Symbol("Theta")

# Die P_0, P_1 und P_2 Funktionen
P0_Equation = "((Theta)**3)-(3*((Theta)**2))+(3*(Theta))-1"
P1_Equation = "(-10)*((Theta)**3)+(10*((Theta)**2))-(3*(Theta))"
P2_Equation = "(9*((Theta)**3))+(9*((Theta)**2))"


# Kurze functions womit ich etwas in die P Funktionen einsetzen kann
# z.B. P_0(i) ist ja einfach die P_0 Funktion wo ich immer statt Theta
# i schreibe.
def p0(theta):
    return P0_Equation.replace("Theta", str(theta))
def p1(theta):
    return P1_Equation.replace("Theta", str(theta))
def p2(theta):
    return P2_Equation.replace("Theta", str(theta))

# Unser Operator
Operator = "P0_Equation + z*P1_Equation + z^2*P2_Equation"

ai = sp.Symbol("ai")
aiminus1 = sp.Symbol("aiminus1")
aiminus2 = sp.Symbol("aiminus2")

# Unsere Rekursion




# Am Anfang haben wir ja 0 und 1
coefficients = [0, 1]

#loop

value_aiminus1 = 1 #a_(i-1)
value_aiminus2 = 0 #a_(i-2)

for i in range(2, 100):
    recursion = "((-1*aiminus2 * {}) - (aiminus1 * {}))/({})".format(eval(p2(i-2)), eval(p1(i-1)), eval(p0(i)))
    this_recursion1 = recursion.replace("aiminus1", str(value_aiminus1)) # a_(i-1) einsetzen
    this_recursion2 = this_recursion1.replace("aiminus2", str(value_aiminus2))# a_(i-2) einsetzen
    this_recursion = str(this_recursion2.replace("i", str(i))) # i einsetzen
    new_ai = eval(this_recursion) # der neue ai Wert der berechnet wurde
    coefficients.append(new_ai) # fügen das zu der Array hinzu
    value_aiminus2 = float(value_aiminus1)
    value_aiminus1 = float(new_ai)




answer = 0 # Das Endergebnis



# Unsere Powerreihe
iter = 0
for j in coefficients:
    answer += int(j)*(float(z)**iter)
    iter+=1

if (answer != 0.06884969710791095):
    raise KeyError("Der Wert stimmt nicht")




print("Answer: " + str(answer)) # Das Ergebnis wird geprintet





    