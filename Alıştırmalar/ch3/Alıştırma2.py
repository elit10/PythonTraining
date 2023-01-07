#dizi içindeki en büyük ve en küçük sayıyı bulan kod

dizi = [-500,0,500,1,2,3,4,5]

max = dizi[0]
min = dizi[0]

for x in dizi:
    if(x > max):
        max = x
    if(x<min):
        min = x

print(max , min)
