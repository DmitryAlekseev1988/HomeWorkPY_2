"""
Задача 12:
 Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает 
 Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
 а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет 
 сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные 
 Петей числа.
4 4 -> 2 2 
5 6 -> 2 3

"""

n1 = int(input("Введите X+Y = "))
n2 = int(input("Введите X*Y = "))

for i in range(1, 1000):
    for j in range(1, 1000):
        if i + j == n1 and i*j == n2:
         print(i, j)
         break
