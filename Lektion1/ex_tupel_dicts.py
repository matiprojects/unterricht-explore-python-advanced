date = (2026, 10, 30)
jahr, monat, tag = date # unpacking

print("Morgen ist der", tag + 1, "igste des Jahres ", jahr)

contact_info = {
"Aliana": "aliana.c@mail.de",
"Amar": "a.y@mail.com"
}

aliana_mail = contact_info["Aliana"]
print(aliana_mail)

contact_info["Aliana"] = "ali.c@mail.de"

print(contact_info)

contact_info ["Ewa"] = "e.w.a@mail.com"
del contact_info["Amar"]

print(contact_info)

keys = contact_info.keys()
values = contact_info.values()
print(keys)
print(values)

items = contact_info.items()
print(items)