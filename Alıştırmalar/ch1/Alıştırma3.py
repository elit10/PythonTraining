#vki hesaplama
# kilo bölü, boyun karesi
# boy metre cinsinden
# kilo / (boy * boy)

kilo = 70
boy = 1.75

vki = kilo / (boy * boy)

if(vki < 18.5):
    print("Zayıf")
elif(vki < 25):
    print("Sağlıklı")
elif(vki < 30):
    print("Kilolu")
else:
    print("Obez")
