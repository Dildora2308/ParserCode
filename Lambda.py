
# x = lambda a, b: a**b

# print(x(2,5))

# items = [3, 2, 10, 21, 23]

# def square(son):
#     return son ** 2

#a = list(map(square, items))


# items = [3, 2, 10, 21, 23]

# # def square(son):
# #     return son ** 2

# a = list(map(lambda son: son **2 , items))
# print(a)




# matnlar = ['python', 'code', 'developer', 'backend']

# def indeks (matn):
#     if len(matn)> 4:
#         return len(matn)
#     return 0
    
# a = list(map(indeks,matnlar))
# print(a)

# a = lambda matn: len(matn) if len(matn) > 4 else 0

# result = list(map(a, matnlar)) ?????
 

# s = ['Python', True, 20, False, None]

# def son (x):
#     if type(x) == int:
#         return True
#     return False
    
#     a = list(filter(son,s))

#     print(a)????



# s = ['Python', True, 20, False, None]
# a = lambda x: True if type(x) == int else False
# result = list(filter(a,s))
# print(result)






# a = list(map(indeks,matnlar))

# print(a)


# matnlar = ['python', 'code', 'developer', 'backend']

# # def indeks ( matn ):
# #     return len(matn)

# a = list(map(lambda matn:len(matn),matnlar))

# print(a)

# from functools import reduce

# result = reduce(lambda x, y: x+y,range(1,101))
# print(result)

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
# x = lambda a, b, c: a + b + c

# result = list(map(lambda a, b, c: a + b + c, a,b,c))

# print(result)


# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]

# def son(a, b, c):
#     return a+b+c

# a = list(map(son,a, b, c))

# print(a)

#2

# color = ['Red', 'Blue', 'Black', 'White', 'Pink']

# # def rang()

# # x = color.split([])

# # result =  list(map)

# print(list(color))


# chars = {'a', 'b', 'E', 'f', 'a', 'i', 'o','U', 'a'}

# a = lambda x: (x.upper(), x.lower())
# def juft(x):
#     return x.upper(), x.lower()

# result = set(map(a,chars))

# print(result)



# #Homework
#4
# student_data = [('Alberto Franco', '15/05/2002','35kg'), 
#                 ('Gino Mcneill','17/05/2002','37kg'), 
#                 ('Ryan Parkes','16/02/1999', '39kg'),
#                 ('Eesha Hinton','25/09/1998', '35kg')]

# ismlar = list(map(lampda x: x[0], student data))
# yillar = list(map(lampda x: x[0], student data))
# kg = list(map(lampda x: x [3],student data))


# nums1 = [1,2,3,4,5,6,7,8]
# nums2 = [2,2,3,1,2,6,7,9]

# result = list(map(lambda x,y: x == y, nums1, nums2))

# print(result.count(True))





