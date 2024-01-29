# - switch variabless
# a = 6
# b = 4
# a,b = b, a
# print(a,b)

# -multiple variable assignment

# a = 4
# b = 3
# c = 6
# a,b,c = 4, 3,6
# print(a,b,c)

# a,b,*c = 4,5,6,7,8
# *a,b,c = 4,5,6,7,8
# *a,b,c = {'x':4, 'y':5, 10:6, 'n':7, 'm':8}
# a,*b,c = "abcdefgh"
# print(a)
# print(b)
# print(c)

# -valros operator exmple :=
# answer = input("Do u want to continue?")
# # while answer == "yes":
# while "y" in answer.lower():
#     x = int(input("Enter a number: "))
#     print(x ** 2)
#     answer = input("Do u want to continue? :")
    
# while "y" in (answer := input("Do u want to continue?")).lower():
#     x = int(input("Enter a number: "))
#     print(x ** 2)

# compare operation
# x = 5
# if 3 < x < 2:
#     print("yes!")
# else:
#     print("no!")

# -most frequent in a loop
# li = [1,2,2,3,2,9,1,3,2]

# def most_frequent(li):
#     counter = 0
#     element = li[0]
#     for num in set(li):
#         frequent = li.count(num)
#         print(num,":",frequent)
#         if frequent > counter:
#             counter = frequent
#             element = num
#     return element
        
# print(most_frequent(li))

# just in one line
# print(max(set(li), key = li.count))
    
    
    
    