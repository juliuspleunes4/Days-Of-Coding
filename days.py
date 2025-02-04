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
def woorden_per_zin():
    zin = input("Geef een zin: ")
    z = zin.split()
    print(len(z))


# woorden_per_zin()
    



"""
Day 7: Write a Python program that asks the user for a word and checks if it is a palindrome 
"""
def palindrome():
    user = input("Geef een woord: ").lower()
    if user[::-1] == user:
        print(f"{user} is WEL een Palindrome!")
    else:
        print(f"{user} is GEEN Palindrome!")

# palindrome()



"""
Day 8: Write a Python program that asks the user for a number and prints the multiplication table (up to 10) for that number.
"""
def multiplication():
    zs = input("Geef een getal: ")
    z = int(zs)
    print(f"{z} * 1 = {z * 1}")
    print(f"{z} * 2 = {z * 2}")
    print(f"{z} * 3 = {z * 3}")
    print(f"{z} * 4 = {z * 4}")
    print(f"{z} * 5 = {z * 5}")
    print(f"{z} * 6 = {z * 6}")
    print(f"{z} * 7 = {z * 7}")
    print(f"{z} * 8 = {z * 8}")
    print(f"{z} * 9 = {z * 9}")
    print(f"{z} * 10 = {z * 10}")

# multiplication()



"""
Day 9: Write a Python program that asks the user for a number and then prints the factorial of that number.
"""
import math

def factorial():
    zs = input("Geef een getal: ")
    s = int(zs)
    z = math.factorial(s)
    print(f"De factorial van {zs} is: {z}")

# factorial()



"""
Day 10: Write a Python program that asks the user for a number and checks if it is a prime number (a number greater than 1 that is only divisible by 1 and itself).
"""
def prime_number():
    z = input("Geef een getal: ")
    zs = int(z)
    
    if zs <= 1:
        print(f"{zs} is NOT a prime number!")
        return
    
    for i in range(2, zs):
        if zs % i == 0:
            print(f"{zs} is NOT a prime number!")
            return
    print(f"{zs} IS a prime number!")

# prime_number()