# 0'dan belirlenen sayıya kadar olan asal sayıları asal.txt isimli bir dosyaya kaydeden kod
file = open("asal.txt" , "w")

sayı = input("sayı giriniz : ")


for i in range(2, int(sayı)):
    asalMı = True
    for j in range(2,i):
        if(i%j == 0):
            asalMı = False
            break
    if(asalMı):
        print(i , "Asal")
        file.write(str(i) + " ")
file.close()