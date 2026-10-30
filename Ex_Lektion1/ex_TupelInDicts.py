zensuren = {
    ("Aliana", "Mathe"): 2,
    ("Amar", "Biologie"): 3,
    ("Aliana", "Physik"): 1
}

amar_biologie = zensuren[("Amar", "Biologie")]
print("Amars zensur in Biologie ist", amar_biologie)

zensuren[("Kilian", "Mathe")] = 4
print(zensuren)

keys = list(zensuren.keys())

student, subject = keys[1]
print(student, "'s Zensur in ", subject, "is ", zensuren[student, subject])

