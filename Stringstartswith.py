bedrijfsnaam = "ITouchables"

bram = ["A","B","C"]
leon = ["D","E","F"]
renier = ["G","H","I"]

for i in bram:
    if bedrijfsnaam.startswith(i):
        print("bram")

for i in leon:
    if bedrijfsnaam.startswith(i):
        print("leon")

for i in renier:
    if bedrijfsnaam.startswith(i):
        print("Renier")

