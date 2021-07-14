# def Salom(name):
#     print (f"Salom {name}")
# ism=input ("ismingizni kiritig: ")
# Salom(ism)
#
# def son ():
#     print(son * 2)
# a =int(input("Raqamni kiriting:"))
# son(a)
#
# def fanlar_ruyxati(*fan):
#     print(fan)
# fanlar_ruyxati("Adabiyot", "Matematika", "ona tili", "Rus tili", "Kimyo")
#
# def rang(r="qora"):
#     print (f"men yoqtirgan rang: {r}")
# rang("oq")
# rang("ko'k")
# rang("sariq")
# rang("qizil")
# rang()
#
# def urta_arifmetik(a,b,c):
#     return (a+b+c)/3
# a=2
# b=1
# c=3
# print(urta_arifmetik (a,b,c))
#
# def katta (a, b):
#     if a>b:
#         return a
#     else:
#         return b
# print(katta(1, 2))
#
# def PowerA3(n):
#     return n**3
# A=1.1
# B=2.2
# C=3.3
# print( PowerA3(A))
# print( PowerA3(B))
# print( PowerA3(C))
# n=int(input("= "))
# def myFunction2(n):
#     qiymat =[]
#     for i in range(1, n):
#         if i ** 2< n:
#             qiymat.append(i)
#         return qiymat
#     print(myFunction2())
# n=int(input("= "))
#
# def n_chiziq(n):
#     for i in range(n):
#
#         print(n * "*")
#
# n_chiziq(n)
# n=int(input("= "))
# def yulduzcha(n):
#      print((n* "*" +'\n')*n)
#
# yulduzcha(n)
# n = int(input("n = "))
#
#
# def buluvchilar(a):
#     for i in range(1, a + 1):
#         if a % i == 0:
#             print(i, end=" ")  # print(i, end="\n") == print(i)
#
#
# buluvchilar(n)
# n =int(input("n ="))
# def rim_raqamlari(n):
#     yuz=n//100
#     un=(n%100)//10
#     bir=n%10
#     if yuz==1:
#         a="C"
#     elif yuz==2:
#         a="CC"
#     elif yuz==3:
#         a="CCC"
#     elif yuz==4:
#         a="CD"
#     elif yuz==5:
#         a="D"
#     elif yuz==6:
#         a="DC"
#     elif yuz==7:
#         a="DCC"
#     elif yuz==8:
#         a="DCC"
#     elif yuz==9:
#         a="CM"
#     elif yuz==0:
#         a=""
#     if un==1:
#         b="XC"
#     elif un==2:
#         b="XX"
#     elif un==3:
#         b="XXX"
#     elif un==4:
#         b="XL"
#     elif un==5:
#         b="L"
#     elif un==6:
#         b="LX"
#     elif un==7:
#         b="VXX"
#     elif un==8:
#         b="LXX"
#     elif un==9:
#         b="XC"
#     elif un==0:
#         b=""
#     if bir==1:
#         c="I"
#     elif bir==2:
#         c="II"
#     elif bir==3:
#         c="III"
#     elif bir==4:
#         c="IV"
#     elif bir==5:
#         c="V"
#     elif bir==6:
#         c="VI"
#     elif bir==7:
#         c="VII"
#     elif bir==8:
#         c="VIII"
#     elif bir==9:
#         c="XC"
#     elif bir==0:
#         c=""
#     print(str(a)+str(b)+str(c))
# rim_raqamlari(n)
# 4-masala
# n =int(input("n ="))
# # yuz=n//100
# # un=(n%100)//10
# # bir=n%10
# # f=yuz+un+bir
# # print(f)
##5-masala
# a =int(input("a ="))
# b =int(input("b ="))
# c =int(input("c ="))
# d =int(input("d ="))
# f =int(input("f ="))
# def engkatta(a, b, c, d, f):
#     katta=max(a, b, c, d, f)
#     return katta
# def engkichik(a, b, c, d, f):
#     kichik=min(a, b, c, d, f)
#     return kichik
# def urtacha(a, b, c, d, f):
#     urtaArt=((a+b+c+d+f)-engkatta(a, b, c, d, f)-engkichik(a, b, c, d, f))/3
#     return urtaArt
# print(f"{engkatta(a, b, c, d, f)}, {engkichik(a, b, c, d, f)}")
# print(urtacha(a, b, c, d, f))
# 6-masala
# n=int(input("n="))
#x=len(str(n))
#print(x)
# rekursiya-> o'ziga murojaat qiladigan funksiya
#1-masala.
# def birdanNgacha(n):
#     if n==1:
#         print(n)
#     else:
#         print(n)
#         birdanNgacha(n-1)
# birdanNgacha(10)
#2-masala
# def n_dan_1_gacha(n):
#     print(n)
#     n_dan_1_gacha(n-1)
# n_dan_1_gacha(10)
#3-masala faktaril
# def fakt(n):
#     if n==1:
#         return 1
#     else:
#         return n*fakt(n-1)
# print(fakt(5))
# 4-masala 1-dan ngacha bulgan sonlar yig'indisi
# def yigindi(n):
#     if n==1:
#         return 1
#     else:
#         return n+yigindi(n-1)
#
# print(yigindi(5))
# #5-masala
# def yigindi_toq(n):
#     if n==1:
#         return 1
#     else:
#         if n% 2 == 0:
#              n=n-1
#         return n+yigindi_toq(n-2)
# print(yigindi_toq(7))
# 6-masala. fibonachi sonlarini n ta xadi chiqaring
# n=int(input("n="))
# a=[]
# a.append(1)
# a.append(1)
# for i in range(n):
#     if i>1:
#         a.append(a[i-1]+a[i-2])
#     else:
#         i+=1
# def fibonachi(n):
#     print(a)
# fibonachi(n)
# SyntaxError
# print("hello",
# # indentionError
# for i in range(5):
#     print(i)
# # NameError
# try:
#     ism="Oybek"
#     print(ims)
# except:
#     print("xato ")
#try: --> urinib ko'rmoq
#except:--> istisno qilish
#7-masala
# y = 0
# try:
#     y = 0
#
#     print("salom")
# except:
#     y += 1
#     print("try dagi nimadur xato")
# finally:
#     if y == 0:
#         print("dasturda xato yo'q")
#     else:
#         print("dasturda xato bor")
#8-masala
# try:
#     n=int(input("n="))
#     if n!=1:
#         raise Exception()
# except:
#     print("xato")
# else:
#     print("xato yo'q")
#9-masala
# try:
#     n=int(input("n="))
#     if n<0:
#         raise Exception ()
# except:
#     print("xato")
# else:
#     print("xato yo'q")
# 3-masala
# try:
#     n=int(input("n="))
#     if n%2==0:
#
#         raise Exception("juft son kiritish mumkim emas")
# except:
#     print("juft son kiritish mumkim emas")
# else:
#     print("siz to'g'ri kiritdingiz")
# finally:
#     print("dastur tugadi")


















