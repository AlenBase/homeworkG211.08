# lis=[]
# for n in range(1,21):
#     if n % 2 == 0:
#         continue
#     elif n % 3 !=0:
#         lis.append(n)
# print(lis)




# user_input = input("input password: ")
# my_password = 'Sayonara'

# while user_input != my_password:
#     test = 0
#     if user_input == my_password:
#         print("Welcome!")
#     elif user_input!= my_password:
#         test+=1
#         print("incorrect, guess again")
#     if test == 3:
#         print("out of guesses")
#         break 





# i=0
# while i<=10:
#     if i ==5:
#         i+=1
#         break
#     print(i)
#     i +=1






# list1=[1,2,3,4,5]
# list2=[3,4,5,6,7]

# result = []
# for n in list1:
#     if n in list2:
#         result.append(n)
# print(result)






# input_string = "Hello, World!"
# for char in input_string:
#     if char == ' ':
#         continue
#     print(char)






# fibonacci_sequence = [0, 1]

# for i in range(2, 10):
#     next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
#     fibonacci_sequence.append(next_number)
# for number in fibonacci_sequence:
#     print(number)






# num = 1
# sum = 0

# while num<=100:
#     if num % 3 == 0 or num % 5 == 0:
#         sum += num
#     num += 1
    
# print(sum)






# num = int(input("Enter a number: "))

# print(f"Multiplication table for {num}:")

# for i in range(1, 11):
#     result = num * i
#     print(f"{num} x {i} = {result}")






# number = int(input("Enter a number: "))

# factorial = 1
# other_num = 1

# while other_num <= number:
#     factorial *= other_num
#     other_num += 1

# print(f"The factorial of {number} is {factorial}")







# score = float(input("Enter the student's score: "))


# S = 100
# A = 91
# B = 81
# C = 61
# D = 41
# E = 21


# if score == S:
#     grade = 'S'
# elif score >= A:
#     grade = 'A'
# elif score >= B:
#     grade = 'B'
# elif score >= C:
#     grade = 'C'
# elif score >= D:
#     grade = 'D'
# elif score >= E:
#     grade = 'E'
# else:
#     grade = 'F'

# print(f"The student's grade is: {grade}")






# sentence = input("Enter a sentence: ")

# vowels = 0
# consonants = 0

# vowel_set = set("AEIOUaeiou")

# for char in sentence:
#     if char.isalpha():
#         if char in vowel_set:
#             vowels += 1
#         else:
#             consonants += 1

# print(f"Number of vowels: {vowels}")
# print(f"Number of consonants: {consonants}")






# squares_dict = {num: num**2 for num in range(1, 101)}

# print(squares_dict)







# powers_of_2 = [2**i for i in range(10)]

# print(powers_of_2)







# number_and_square = [(num, num**2) for num in range(1, 11)]

# print(number_and_square)





a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# discriminant = b**2 - 4*a*c

# if discriminant > 0:
#     x1 = (-b + (discriminant ** 0.5)) / (2*a)
#     x2 = (-b - (discriminant ** 0.5)) / (2*a)
#     print(f"The roots are real and distinct: x1 = {x1}, x2 = {x2}")
# elif discriminant == 0:
#     x1 = -b / (2*a)
#     print(f"There is one real root: x1 = {x1}")
# else:
#     real_part = -b / (2*a)
#     imaginary_part = (abs(discriminant) ** 0.5) / (2*a)
#     print(f"The roots are complex: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i")

