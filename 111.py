# yil  = int (input("uquvchining yilini kiriting yilni kiriting "))
# shaxs = {
#     "ism": "Otabek",
#     "yoshi": 10,
#     "uquvchi": False ,
#     "uquvchi2": True
# }
# if shaxs["yoshi"] + yil > 18:
#     print(shaxs["uquvchi"])
# elif shaxs["yoshi"] + yil < 18:
#      print(shaxs["uquvchi2"])

# talaba={
#     "ism":"Oybek",
#     "Yosh": 22,}
# for i in talaba:
#     if i=="Yosh":
#         print("bor")
#         break
# else:
#     print("Yo'q")

suz=input("Inglizcha so'z kiriting-")
suz=suz.lower()
EnUz=    {
    "I": "Men",
    "You": "Siz",
    "Hello": "Salom"
}
if suz in EnUz.keys():
    print(EnUz [suz])
else:
    print("Bunday so'z lug'atda yo'q")



