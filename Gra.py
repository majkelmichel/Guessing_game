from random import randint

def plik():
    f = open("words.txt", "r")
    contents = f.readlines()
    return contents

def losuj_slowo(slowa):
    a = randint(1,999)
    slowo = slowa[a]
    return slowo

def dlugosc_slowa(slowo):
    zgadywanie = ""
    for i in slowo:
        zgadywanie += "_"
    return zgadywanie

def zgadywanie(slowo):
    guess = input("Podaj litere: ")
    while guess not in 'abcdefghijklmnopqrstuvwxyz':
        print("Zły znak")
        guess = input("Podaj litere: ")
    return guess

word = plik()
slowo = losuj_slowo(word)
dl = dlugosc_slowa(slowo)
print(slowo)
x=0
lb_prob = 0
ukryte = []

for i in range(len(slowo) - 1):
    ukryte.append("_")
while '_' in ukryte:
    indexy = []
    string = ''
    x=0
    guess = zgadywanie(slowo)
    for i in slowo:
        if guess == i:
            indexy.append(x)
        elif guess == slowo:
            string = slowo
            print("dziala")
            break
        x+=1
    for j in indexy:
        ukryte.insert(j,slowo[j])
        ukryte.pop(j+1)
    for i in ukryte:
        string += i
    print(string)
    lb_prob+=1

print("Gratulacje. Udało ci się odgadnąć słowo.")
print("Potrzebowałeś na to %s prób." % (lb_prob))