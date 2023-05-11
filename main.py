import math


def addPoint(P, Q, p):
    s = (int((Q[1] - P[1]) / (Q[0] - P[0]))) % p
    x_3 = (math.pow(s, 2) - P[0] - Q[0]) % p
    y_3 = (s * (P[0] - x_3) - P[1]) % p

    return [x_3, y_3]


def doublePoint(P, Q):
    print("Todo")


a = int(input("Parameter a: "))
b = int(input("Parameter b: "))
p = int(input("Primzahl p: "))

print("Hinweis: Punkt muss die Form x,y haben")
P = input("Punkt P: ").replace(" ", "").split(",")
Q = input("Punkt Q: ").replace(" ", "").split(",")

# in integers umwandeln
P[0] = int(P[0])
P[1] = int(P[1])
Q[0] = int(Q[0])
Q[1] = int(Q[1])

# Todo entscheiden ob Addition oder Verdopplung
# TODO Parameterprüfung: Länge von P und Q muss 2 sein

# Fallunterscheidung, ob eine Punktaddition oder eine Punktverdopplung stattfinden muss
# Es wird eine Punktverdopplung durchgeführt, wenn beide Punkte die selben Koordinaten haben.

if P[0] == Q[0] and P[1] == Q[1]:
    print(f"Punkt P {P} und Q {Q} sind gleich. Es wird eine Punktverdopplung durchgeführt.")
else:
    print(f"Punkt P {P} und Q {Q} sind nicht gleich. Es wird eine Punktaddition durchgeführt.")
    R = addPoint(P, Q, p)
    print(R)

