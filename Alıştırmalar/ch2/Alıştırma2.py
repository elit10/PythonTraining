# girilen sayının faktöriyeli
# 1 * 2 * 3 * ....  * n = n!

def faktoriyel(n,v):
    if(n == 1):
        print("faktöriyel == " + str(v))
    else:
        v *= n
        faktoriyel(n-1,v)

faktoriyel(6,1)