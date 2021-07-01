# import random
# for i in range (10):
#     print (random.random())

# kiritilganSon = int(input("son->"))
# tasodifiySon = random.randint(1,5)
# if kiritilganSon == tasodifiySon:
#     print(tasodifiySon)
#     print("Yutdingiz")
# else:
#     print("tasodifiySon")
#     print("Dam oling")

import random
while True:
    tasodifiySon = random.randint(1,4)
    kritilganSon = int(input("son->"))
    if kritilganSon == tasodifiySon:
        print("Yutdingiz")
        break
    else:
        print("Omadingiz kelmadi")


