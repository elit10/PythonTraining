# 3-4-5. hafta

#Recursion
def loop():
    print("ne")
    loop()

#loop()

def what():
    print("Ne demek?")
    print("Ben de onu diyorum ne demek?")
    what()

print("What ne demek?")
#what()

def zikirmatik(z):
    z+=1
    print("bismillah x" + str(z))
    zikirmatik(z)

#zikirmatik(0)

def komik(s):
    print(s)
    if(s == 31):
        print(":D")
    else:
        s+=1
        komik(s)

#komik(0)

# ---Alıştırma 1---
#100'e kadar 7'şer 7'şer sayan kod

# INPUT
print("Input okuma")

#input("Bir değer giriniz: ")

#cevap = input("İsiminiz nedir? :")

#print("adınız " + cevap)

#x = input("X değeri giriniz :")

#print(int(x) + 5)


def SayMyName(count, name):
    if(count != 0):
        print(name)
        SayMyName(count - 1, name)


#count = input("kaç kere yazalım ? : ")

#SayMyName(int(count), "Heisenberg")

#  ---Alıştırma 2--- (zor)
# girilen sayının faktöriyelini hesaplayan kod


# DÖNGÜLER
print("DÖNGÜLER")

for x in range(10):
    print(x)

for x in range(20,30):
    print(x)

for x in range(0,100,7):
    print(x)

for x in range(100, 0, -7):
    print(x)

toplam = 0
for x in range(0):
    v = input("değer giriniz :")
    toplam = toplam + int(v)

print(toplam)

# ---Alıştırma 3---
# Heisenberg örneği ama for loop ile


# While loop
print("While loop")

x = 0
while(x < 100):
    x+=1
    print(x)


print("break kullanımı")
x = 50
while(True):
    x = x-1
    print(x)
    if(x < 0):
        break

# ---Alıştırma 4---
#Heisenberg örneği ama while loop ile