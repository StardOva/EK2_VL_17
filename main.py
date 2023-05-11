import math

def addPoint(P, Q, p):
    s_zaehler = (Q[1] - P[1]) % p
    print("s_zaehler", s_zaehler)

    s_nenner = (Q[0] - P[0]) % p
    print("s_nenner", s_nenner)

    s_inverse = math.pow(s_nenner, p-2)
    print("s_inverse", s_inverse)

    s = (s_zaehler * s_inverse) % p

    print("s =", s)

    x_3 = float((math.pow(s, 2) - P[0] - Q[0]) % p)
    y_3 = float((s * (P[0] - x_3) - P[1]) % p)

    return [x_3, y_3]


def doublePoint(P, Q):
    print("Todo")


a = float(input("Parameter a: "))
b = float(input("Parameter b: "))
p = float(input("Primzahl p: "))

print("Hinweis: Punkt muss die Form x,y haben")
P = input("Punkt P: ").replace(" ", "").split(",")
Q = input("Punkt Q: ").replace(" ", "").split(",")

# in integers umwandeln
P[0] = float(P[0])
P[1] = float(P[1])
Q[0] = float(Q[0])
Q[1] = float(Q[1])

# TODO Parameterprüfung: Länge von P und Q muss 2 sein

# Fallunterscheidung, ob eine Punktaddition oder eine Punktverdopplung stattfinden muss
# Es wird eine Punktverdopplung durchgeführt, wenn beide Punkte die selben Koordinaten haben.

if P[0] == Q[0] and P[1] == Q[1]:
    print(f"Punkt P {P} und Q {Q} sind gleich. Es wird eine Punktverdopplung durchgeführt.")
else:
    print(f"Punkt P {P} und Q {Q} sind nicht gleich. Es wird eine Punktaddition durchgeführt.")
    R = addPoint(P, Q, p)
    print(R)
