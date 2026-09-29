a=0
b=0
c=0
while c<=14 :
    a = 2**c
    b = a * 1.61 #conversion en dollars canadiens
    c = c+1
    print(str(a) + "€ = " + str(b) + " $CAD")