#1

# for i in range(1500,2700)
# if i  % 35 == 0:
#     Print(i)
    

 
# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0,-1), [5, 12],{"class":'V', "section":'A'}]
# for i in datalist:
#      print(f"Type of {i} is {type}")

#4

# for x in range(0,7):
# if x == 3 , 6:
#     continue
#     print(x)

#5

# matn = input("matn kiriting:")

# harf = sum(c.isalpha() for c in matn)
# raqam = sum(c.isdigit() for c in matn)

# print("Harflar soni:",harf)
# print("Raqamlar soni:",raqam)

#7

# Son_kiriting = int(input("Butun son kiriting:"))

# print(son_kiriting)
# for x in range(1,10):
#     karra = Son_kiriting * x
#     print("{} * {} = {}".format(Son_kiriting, x, karra))


# 9


# for i in range(7):
#         for j in range(7):
#             if i in [0,6] or i + j ==5:
#                 print("*", end="")
#             else:      
#                  print(" ", end="")  
#         print("")   


# for i in range(7):
#       for j in range(7):
#             if i in [0,6] or i + j ==5:
#                 print("*", end="")
#             else:      
#                 print(" ", end="")  
#        print("")   


# row = 3  # ustun va qator ko'paytmasi
# column = 4
# result = []

# for i in range (row):
#     a = []
#     for j in range(column):
#         a.append(i*j) #[0,0,0,0]
#     result.append(a)

# print(result)






#while loop

# print('Kiritilgan sonning kvadratini qaytaruvchi dastur')
# savol = 'Istalgan son kiriting'
# savol += "(Dasturni to'xtatish uchun'exit' deb yozing)"
# qiymat = ' '
# while  qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print('Dastur tugadi')


# Ask the user to enter a text
text = input("Enter some text: ")

# Initialize variables
reverse_text = ""
index = len(text) - 1

# Reverse the text using a while loop
while index >= 0:
    reverse_text += text[index]
    index -= 1

# Print the reversed text
print("Reversed text:", reverse_text)











