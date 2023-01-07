#1-2-3. hafta

x = type(11)
#11'in obje türünü x değişkenine yerleştiriyoruz
y = type(1.5)
z = type("deneme")

print(x)
#bu obje türünü ekrana yazdırıyoruz
print(y)
print(z)

#değişkenlerin içeriğini değiştiriyoruz

x = "selam"
y = 5
z = 3.7

# x + y + z yazarsak sistem bize hata verecek

print(x + str (y) + str(z))
#type casting yaparak y ve z'yi stringe çevirdik, daha sonrasında ekrana yazdırdık



print(type(str(15)))
#type casting örneği

print(int(99.9999))
#virgülden sonra gelen basamaklar çöpe gidiyor

#print(int ("deneme"))
#  "deneme" değeri bir tam sayı olmadığı için valueError alacağız

print(int("123"))

print("Send /nudes")
print("Send \nudes")

print("\"vah vah\" dedi kadın")

# ---Alıştırma 1---
#1 den 100'e kadar olan sayıların toplamını bulan python kodu

# KÜTÜPHANE
print("KÜTÜPHANE")

import math

karekok = math.sqrt(25)
kare = math.pow(5, 2)
taban = math.floor(3.9)
tavan = math.ceil(2.1)
#matematik operasyonları

print(karekok)
print(kare)
print (taban)
print(tavan)



#       ARİTMETİK OPERASYONLAR
print("ARİTMETİK OPERASYONLAR")

print(14/5)
#dümdüz bölme, float type döndürür

print(14//5)
#int type cast ile bölme

print(14%5)
#mod hesabı

print(5 * 5)
#çarpma

print(2**6)
#üslü sayılar

print("deneme " + "123")
#string ile toplama

x = 5
x+=2

print(x)
#+= -= *= /= ile operasyonlar yapılabilir


#       MANTIKSAL İŞLEMLER
print("MANTIKSAL İŞLEMLER")

x = 5
y = 10

print(x == 5)
print(y == 10)

print(x == y)
print(x != y)
# aritmetik eşitlik kullanarak değişkenlerin değerlerini kontrol ettik ( 5 ve 10 birbirine eşit değil)

print("büyüklük - küçüklük")

print(x > y)
print(x < y)
#büyüklük küçüklük kıyası
print(5 < 10)
#ikisi arasında bir fark yok

print(5<= 10)
print(5>= 10)
print(5 != 10)

print("AND ve OR operasyonları")

print( 5 < 10 and 3 > 2)
# and operasyonu iki koşulun da doğru olmasını ister

print( True and False)
# herhangi bir değer FALSE ise and operasyonu false döndürecektir

print( 5 < 10 or 2 > 3)
#  or operasyonu için bir koşulun sağlanması yeterli

print(True and False)
#OR Herhangi bir değer TRUE ise or operasyonu true döndürecek

# eşittir her zaman SAĞDA

# FONKSİYONLAR
print("FONKSİYONLAR")

def cayciHuseyin():
    print("Çaylarrr")


cayciHuseyin()
#tanımlı fonksiyonu çağırdık


def daireAlanı(r):
    print("bu dairenin alanı = " + str(math.pi * r * r))

daireAlanı(3)

# ---Alıştırma 2---
#kenar uzunluğu verilen küpün hacmini hesaplayan fonksiyon

# KARAR OPERASYONLARI (IF ELIF ELSE)
print("IF ELSE")

dünya = 4

if( dünya > 5):
    print("dünya 5'ten büyüktür")
else:
    print("eeeyyy")

dersNotu = 91

if(dersNotu > 85):
    print("A")
elif(dersNotu > 70):
    print("B")
elif(dersNotu > 55):
    print("C")
elif(dersNotu > 35):
    print("D")
else:
    print("F")

dedigim = "Ayşe"

if(dedigim == "Ayşe"):
    print("yengeye doğru dedin usta")

elif(dedigim == "Elif"):
    print("yengeye Elif dedin usta")

else:
    print("Yengeye ne dedin usta")

#   ---Alıştırma 3---
# vki hesaplama









