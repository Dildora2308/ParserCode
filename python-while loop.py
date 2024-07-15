# for i in range(1,6)
#   print(i)



# i = 1
# while i <= 5:
#         print(i)
#         i+=1


# i = 2  #faqat juft
# while i< 11:
#     print(i)
#     i+=2  

# age = 32
# while age >18:
#     print('you can vote') # cheksiz aylanish


# darsda 
# import random

# kompyuter_oylagan_son = random.randrange(1,11)
# urinishlar_soni = 0
# print("kompyuter son oyladi siz uni topishingiz kerak!!!")

# biz_oylagan_son = int(input('kompyuter oylagan sonni kiriting:'))

# while biz_oylagan_son != kompyuter_oylagan_son:
#     urinishlar_soni += 1
#     print('san oylagan son xato , qaytadan orinib kor')
#     biz_oylagan_son = int(input('kompyuter oylagan sonni kiriting:'))
# else:
#     print(f'Tabriklaymiz siz kompyuter oylagan sonni topdingiz,{kompyuter_oylagan_son},urinishlar soni: {urinishlar_soni1}')

# import random

# biror_son_oylang = int(input('1 dan 10 gacha biror son o"ylang: '))
# urinishlar_soni = 0
# print("son o'ylandi")
# kompyutr_son_topsin = random.randrange(1,11)

# while biror_son_oylang != kompyutr_son_topsin:
#     urinishlar_soni +=1
#     print("kompyuter o'ylagan son xato,qayta urinish")
#     kompyutr_son_topsin = random.randrange(1,11)
# else:
#     print(f'Tabriklaymiz Kompyuter sonni topdi: {kompyutr_son_topsin},urinishlar soni:{urinishlar_soni}')


import random

biror_son_oylang = int(input('1 dan 10 gacha biror son o"ylang: '))
urinishlar_soni = 0
print("son o'ylandi")
kompyutr_son_topsin = random.randrange(1, 11)

while biror_son_oylang != kompyutr_son_topsin:
    urinishlar_soni += 1
    print("kompyuter o'ylagan son xato, qayta urinish")
    kompyutr_son_topsin = random.randrange(1, 11)
else:
    print(f'Tabriklaymiz! Kompyuter sonni topdi: {kompyutr_son_topsin}, urinishlar soni: {urinishlar_soni}')








 
   