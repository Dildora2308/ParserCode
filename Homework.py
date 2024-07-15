#python loop
#1
# i = 1
# while i <= 10:
#     print(i)
#     i+= 1

# #2
# yigindi = 0 # yig'indini hisoblash uchun o'zgaruvchi va qiymat 0
# i = 1
# raqam = int(input('Raqam Kiriting:'))

# while i <= raqam:
#     yigindi += i
#     i += 1
# print(f'{raqam} gacha raqamlar yigindisi: {yigindi} ')

#  1 dan boshlab kiritilgan raqamgacha 1 qo'shib ketaveradi va yig'indiga yig'adi. 

#3

# while True:
#     son = int(input('Son kiriting:'))
#     if son % 2 != 0:
#         print('Toq raqam kiritildi, iltimos bshqa raqam kiriting:')
#     else:
#        print('juft raqam kiritildi')
#        break


#4
# matn = 'While loop'
# i = 0

# while i < len(matn):
#     print(matn[i])
#     i +=1

#5



# while True:

#     matn = str(input('Matn kiriting: '))
#     if va in matn:
# print('Bor')

#         matn = str(input('qayta matn kiriting:'))
#     else:
#         print('bor')



# intermediate

# 2
# import random

# siz_oylagan_son = int(input('Biror son o\'ylang: ')) 

# urinishlar_soni = 0

# print('Siz o\'ylagan sonni kompyuter topadi')

# kompyuter_oylagan_son = random.randrange(1,11)

# while kompyuter_oylagan_son != siz_oylagan_son:
#     urinishlar_soni += 1
#     print('kompyuter xato o\'yladi, qayta kiritish kerak!')
#     kompyuter_oylagan_son = random.randrange(1,11)
# else:
#    print(f"Qoyil! kompyuter topdi!, {siz_oylagan_son}, urinishlar soni: , {urinishlar_soni}")


#3
# son = int(input('Son kiriting: '))


# juft_yigindi = 0
# i = 1
# son = int(input('Son kiriting: '))

# while i <= son:
#        juft_yigindi += i
#        i += 1



# 3
# son = int(input('Son kiriting:'))
# juft_yigindi = 0
# i = 0
# while i <= son:
#      if i % 2 == 0:
#         juft_yigindi += i
#      i += 1
# print(f"{son}gacha juft sonlar yig'indisi:{juft_yigindi}")

#
#son = int(input('Son kiriritng:'))

# while True:
#     if son % 2 == 1:

#else:
#      print('tub son')


# 5 
# faktorial = 1 # faktorial hisoblash uchun o'zgaruvchi va qiymat 0
# i = 1
# raqam = int(input('Raqam Kiriting:'))

# while i <= raqam:
#     faktorial *= i
#     i += 1
# print(f'{raqam} faktoriali: {faktorial} ')

#  1 dan boshlab kiritilgan raqamgacha 1 qo'shib ketaveradi va ko'paytmaga  yig'adi.




#Funksiyalar

a,b,c = 4, 3, 5
def my_max(a,b):
    if a > b:
        return a
    return b
result = my_max(my_max(a,b),c)





    

