cajeSemana = int(input("Cuantas cajetillas consume semanalmente?: "))
VRCIG = int(144000 / (40 * 12))
cantCig = cajeSemana * 12 * 48
diGastado = VRCIG * cantCig
print((cantCig * 3), diGastado)

if (cantCig * 3) > 4000 and diGastado > 300000:
    print("alto")
else:
    print("medio")
