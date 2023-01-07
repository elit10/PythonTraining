x = "Python Dersi Yapıyoruz"

print(x.upper())
print(x.lower())

print(x.find("o"))
#ilk olanı bulur (en solda)

print(x.find("o" , 5))

f = open("names.txt","w")

# w ---> write
# a ---> append
# r ---> read


f.write("Onur")

f.close()

file = open("data.txt" , "w")

file.write("Deneme1")
file.write("Deneme2")

file.close()

file = open("data.txt" , "w")

for i in range (10):
    file.write(str(i))

file.close()

file = open("data.txt", "r")

x = file.read()
print(x)

# ---Alıştırma 1---
# 0'dan belirlenen sayıya kadar olan asal sayıları asal.txt isimli bir dosyaya kaydeden kod


import os

x = os.listdir()
print(x)

x = os.listdir("c:/")
print(x)

x = os.listdir("C:/Users/onurs/Documents/GitHub/PythonTraining/Dersler")
print(x)