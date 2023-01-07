# 100'e kadar 7şer 7şer yazan kod

def say(x):
    if(x>100):
        print(str(x) + " son sayı")
    else:
        x += 7
        print(x)
        say(x)

say(0)