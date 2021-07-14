x = lambda  a: a**5
print(x(2))

urta_arifmetik = lambda a,b,c,d: (a+b+c+d)/4
print(urta_arifmetik(10,20,20,30))

def aylana (L):
    return lambda pi: pi * (L/(2*pi))**2
x = aylana(10)
print(x(5.45))

def ism (i):
    return lambda n: (i+' ')*n
k=input("ism kiriting-")
n_ta_ism =ism(k)
print(n_ta_ism(5))