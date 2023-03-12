N = float(input("дължината на площадката: "))
W = float(input("широчината на една плочка: "))
L = float(input("дължината на една плочка: "))
M = float(input("широчината на пейката: "))
O = float(input("дължината на пейката: "))
peika = M*O
plochka = W * L
ploshtadka = (N*N) - peika
broiki = ploshtadka / plochka
vreme = broiki*0.2
print(f"Broi plochki:",broiki)
print(f"Vreme: ", vreme)
