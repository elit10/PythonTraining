#5-6-7. hafta

dizi = [1,2,3,4,5]
isimler = ["Onur" , "Ali" , "Selin"]

print(dizi)
print(isimler)

print(dizi[0])
print(isimler[2])


print(len(isimler))


print(isimler[len(isimler) - 1])

print(isimler[-1])

for ad in isimler:
    print(ad)

#pass by value vs referance
print(dizi)
for num in dizi:
    num *= 2
    print(num)
print(dizi)

for x in range(len(dizi)):
    dizi[x] *= 2
    print(dizi[x])
print(dizi)

print(dizi[2:4])
print(dizi[2:])
print(dizi[:4])

x = "James"

delimeter = " | "

t = delimeter.join(x)

print(t)

dizi.append(12)
print(dizi)

dizi2 = [1,2,3,4,5]

dizi.extend(dizi2)

print(dizi)

dizi.sort()

print(dizi)

dizi.pop(1)

print(dizi)

popped = dizi.pop(3)

print(str (popped) + " rakamını listeden attık" )
print(dizi)

del dizi[1]
print(dizi)

del dizi[2:4]
print(dizi)


tablo = "Onur , 123 , Ahmet , 321 , Emir , 131"

düzenliTablo = tablo.split(" , ")

for eleman in düzenliTablo:
    print(eleman)


#Dict
print("Dict")

Arabalar = {
  "uretici": "Renault",
  "model": "Clio",
  "yil": 2009
}
print(Arabalar)

Arabalar["yil"] = 2020

print(Arabalar)

Arabalar["fiyat"] = 300000

print(Arabalar)

yil = Arabalar.pop("yil")
print(Arabalar)
print(yil)

#Binary