def addPoint(P, Q):
    print("Todo")

def doublePoint(P, Q):
    print("Todo")


a = int(input("Parameter a: "))
b = int(input("Parameter b: "))
p = int(input("Primzahl p: "))

print("Hinweis: Punkt muss die Form x,y haben")
P = input("Punkt P: ").replace(" ", "").split(",")
Q = input("Punkt Q: ").replace(" ", "").split(",")

# TODO Parameterprüfung: Länge von P und Q muss 2 sein

# Fallunterscheidung, ob eine Punktaddition oder eine Punktverdopplung stattfinden muss
# Es wird eine Punktverdopplung durchgeführt, wenn beide Punkte die selben Koordinaten haben.

if P[0] == Q[0] and P[1] == Q[1]:
    print(f"Punkt P {P} und Q {Q} sind gleich. Es wird eine Punktverdopplung durchgeführt.")
else:
    print(f"Punkt P {P} und Q {Q} sind nicht gleich. Es wird eine Punktaddition durchgeführt.")


