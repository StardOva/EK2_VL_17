import math


def power(base, exponent, p):
    result = base
    for x in range(exponent - 1):
        result = math.pow(result, 2) % p
        print(str(result))

    return result


def addPoint(P, Q, p):
    s_zaehler = (Q[1] - P[1]) % p
    print("s_zaehler", s_zaehler)

    s_nenner = (Q[0] - P[0]) % p
    print("s_nenner", s_nenner)

    s_inverse = power(s_nenner, p - 2, p)
    print("s_inverse", s_inverse)

    s = (s_zaehler * s_inverse) % p

    print("s =", s)

    x_3 = int((math.pow(s, 2) - P[0] - Q[0]) % p)
    y_3 = int((s * (P[0] - x_3) - P[1]) % p)

    return [x_3, y_3]

    # Zähler und Nenner mod p rechnen

def doublePoint(P, a, p):
    # s = (y2-y1)/(x2-x1) mod p berechnen
    # Zähler und Nenner werden erst einzeln berechnet
    s_zaehler = (3*(P[0] * P[0]) + a) % p
    s_nenner = (P[1] + P[1]) % p

    s_inverse = math.pow(s_nenner, p - 2)
    print("s_inverse", s_inverse)

    s = (s_zaehler * s_inverse) % p

    print("s =", s)

    x_3 = float((math.pow(s, 2) - P[0] - Q[0]) % p)
    y_3 = float((s * (P[0] - x_3) - P[1]) % p)

    return [x_3, y_3]


#print(str(power(12, 9, 11)))

a = int(input("Parameter a: "))
b = int(input("Parameter b: "))
p = int(input("Primzahl p: "))

P_unendlich = False
Q_unendlich = False

print("Hinweis: Punkt muss die Form x,y haben")
P = input("Punkt P: ").replace(" ", "")
if "," in P:
    P = P.split(",")
elif P == "O":
    P_unendlich = True

Q = input("Punkt Q: ").replace(" ", "")
if "," in Q:
    Q = Q.split(",")
elif Q == "O":
    Q_unendlich = True

# Behandlung vom Punkt in der Unendlichkeit
if P_unendlich and not Q_unendlich:
    print("P dient als neutrales Element, Ergebnis ist Q = ", Q)
elif not P_unendlich and Q_unendlich:
    print("Q dient als neutrales Element, Ergebnis ist P = ", P)
elif P_unendlich and Q_unendlich:
    print("Beide Elemente sind das neutrale Element, Ergebnis ist O")
else:

    # in integers umwandeln
    P[0] = int(P[0])
    P[1] = int(P[1])
    Q[0] = int(Q[0])
    Q[1] = int(Q[1])

    # TODO Parameterprüfung: Länge von P und Q muss 2 sein

# Fallunterscheidung, ob eine Punktaddition oder eine Punktverdopplung stattfinden muss
# Es wird eine Punktverdopplung durchgeführt, wenn beide Punkte dieselben Koordinaten haben.

if P[0] == Q[0] and P[1] == Q[1]:
    print(f"Punkt P {P} und Q {Q} sind gleich. Es wird eine Punktverdopplung durchgeführt.")
    R = doublePoint(P, a, p)
    print(R)
else:
    print(f"Punkt P {P} und Q {Q} sind nicht gleich. Es wird eine Punktaddition durchgeführt.")
    R = addPoint(P, Q, p)
    print(R)
