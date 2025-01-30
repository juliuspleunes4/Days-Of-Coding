"""
PYTHON: 365 DAYS OF CODING CHALLENGE
Gedurende het jaar zal de moeilijkheid van beginner tot geavanceerd gaan!
"""


"""
Day 1: Schrijf een Python-programma dat een getal van de gebruiker vraagt, en vervolgens het kwadraat van dat getal berekent en toont.
"""
def kwadraat_van_input():
    getal = int(input("Geef een getal: "))
    print(f"Het kwadraat van {getal} is {getal**2}")

# kwadraat_van_input()


"""
Day 2: Schrijf een Python-programma dat de gebruiker vraagt om een getal, en vervolgens toont of het getal even of oneven is.
"""
def getal_vragen():
    user_input = input("Geef een getal: ")
    user_input = int(user_input)
    if user_input % 2 == 0:
        print(f"{user_input} is een EVEN getal")
    else:
        print(f"{user_input} is een ONEVEN getal")

# getal_vragen()


"""
Day 3: Schrijf een Python-programma dat de gebruiker vraagt om een getal, en vervolgens toont of het getal positief, negatief of nul is.
"""
def getal_waarde():
    opvragen = input("Geef een getal: ")
    opvragen = float(opvragen)
    if opvragen == 0:
        print(f"{opvragen} is gelijk aan 0!")
    if opvragen > 0:
        print(f"{opvragen} is een POSITIEF getal!")
    if opvragen < 0:
        print(f"{opvragen} is een NEGATIEF getal!")

# getal_waarde()


"""
Day 4: Schrijf een Python-programma dat de gebruiker vraagt om een getal, en vervolgens toont of het getal een veelvoud is van 5.
"""
def veelvoud_getal():
    gebruiker = input("Geef een getal: ")
    gebruiker = int(gebruiker)
    if gebruiker % 5 == 0:
        print(f"{gebruiker} is WEL een veelvoud van 5!")
    else:
        print(f"{gebruiker} is NIET een veelvoud van 5!")


# veelvoud_getal()


"""
Day 5: Schrijf een Python-programma dat de gebruiker vraagt om een woord, en vervolgens dat woord omdraait en toont.
"""
def woord_draaier():
    woord = input("Geef een woord: ")
    print(woord[::-1])


# woord_draaier()



"""
Day 6: Write a Python program that asks the user for a sentence and then counts how many words are in the sentence.
"""