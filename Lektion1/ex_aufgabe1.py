aliana_contact = {
    "Name" : "Aliana",
    "Telefonnummer": "0137486655",
    "Email" : "liana@mail.com"
}

amar_contact = {
    "Name" : "Amar",
    "Telefonnummer": "014444896",
    "Email" : "a.m.@mail.com"
}

contacts = {
    "Aliana": aliana_contact,
    "Amar": amar_contact
}

print("Alianas Kontakt information:")
print(contacts["Aliana"])

contacts["Amar"]["Telefonnummer"] = "2059999666"

print("\nAmars updated Kontaktinformation: ")
print(contacts["Amar"])