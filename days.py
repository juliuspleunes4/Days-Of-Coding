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



"""
Day 11: Write a Python program that generates a random number between 1 and 100 and asks the user to guess it. The program should give hints if the guess is too high or too low.
"""
import random

def random_number():
    goofy_ahh = random.randint(1, 100)
    while True:
        hoi = input("Geef een random getal tussen de 1 en 100: ")
        blehh = int(hoi)
        if blehh == goofy_ahh:
            print(f"Gefeliciteerd! Het was inderdaad {goofy_ahh}")
            break
        if blehh > goofy_ahh:
            print("Te hoog!")
        else:
            print("Te laag!")

# random_number()
    


"""
Day 12: Write a Python program that takes a list of numbers as input and prints the largest number in the list.
"""
def largest_number():
    zs = input("Geef een lijst getallen (voorbeeld: 1 3 8 20 7): ")
    gesplit = list(map(int, zs.split()))
    gesplit.sort()
    ding = gesplit[-1]
    print(f"Grootste getal = {ding}")

# largest_number()





"""
Day 13: Write a Python program that removes all duplicate numbers from a list while keeping the original order.
"""
def duplicates_remover():
    list = [1, 5, 4, 5, 7, 2, 7, 6]
    leeg = []
    for i in list:
        if i not in leeg:
            leeg.append(i)
    print(leeg)



# duplicates_remover()



"""
Day 14: Write a Python program that finds the second largest number in a list of numbers.
"""
def second_largest():
    list = [1, 3, 2, 8]
    list.sort()
    list.reverse()
    zs = list[1]
    print(zs)

# second_largest()



"""
Day 15: Write a Python program that checks if two strings are anagrams (contain the same letters in a different order, like "listen" and "silent").
"""
def anagram_checker():
    str1 = "Listen"
    str2 = "Silent"

    bla = str1.lower()
    bluh = str2.lower()

    if sorted(bla) == sorted(bluh):
        print("Anagram!")
    else:
        print("GEEN Anagram!")
        
# anagram_checker()



"""
Day 16: Write a Python program that finds the most frequent element in a list.
"""
def most_frequent_element():
    nums = [1, 3, 7, 1, 3, 7, 7, 2, 5, 2, 5, 5, 5, 5, 5]
    print(max(set(nums), key=nums.count))


# most_frequent_element() 

    


"""
Day 17: Write a Python program that finds the longest word in a sentence given by the user.
"""
def longest_word():
    user_input = input("Geef een string: ")
    gesplit = user_input.split()
    grootste = ""
    for word in gesplit:
        if len(word) >= len(grootste):
            grootste = word
    print(grootste)

# longest_word()




"""
Day 18: Write a Python program that counts how many vowels (a, e, i, o, u) are in a given sentence.
"""
def vowels():
    z = "Hallo, ik ben Julius!"
    leeg = []
    for letter in z:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            leeg.append(letter)
    print(len(leeg))

# vowels() 




"""
Day 19: Write a Python program that takes a list of numbers and returns a new list with only the even numbers.
"""
def even_numbers():
    number = [3, 12, 7, 8, 15, 23, 42, 17, 19, 29, 10, 6]
    z = []
    for num in number:
        if num % 2 == 0:
            z.append(num)
    print(z)

# even_numbers()




"""
Day 20: Write a Python program that takes a list of numbers and returns a new list where each number is squared.
"""
def list_squared():
    list = [2, 5, 8, 3, 7, 12, 15, 6]
    z = []
    for item in list:
        item = item ** 2
        z.append(item)

    print(z)

# list_squared()



"""
Day 21: Write a Python program that reverses the words in a given sentence while keeping their original order.
"""
def reverse_words_og():
    sentence = "Hallo, ik ben Julius!"
    empty = []
    z = sentence.split()
    for i in z:
        i = i[::-1]
        empty.append(i)
    print(*empty)

reverse_words_og()





"""
Day 22: Write a Python program that removes all punctuation from a given sentence.
"""