
# ? DICTIONARIES
# months = {
#     "January": 31,
#     "February": 28,
#     "March": 31,
#     "April": 30,
#     "May": 31,
#     "June": 30,
#     "July": 31,
#     "August": 31,
#     "September": 30,
#     "October": 31,
#     "November": 30,
#     "December": 31

# # }
# months = {
#     1 : 31, 

# month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# print(months["July"])


# def calculator(num1, num2, operands):
#     num1 = 2
#     num2 = 5
#     operands = {
#     'add': num1 + num2,
#     'substract' : num1 - num2,
#     'multiply': num1 * num2,
#     'devide': num1 / num2


# }
#     return operands 
# signs = { 'add': '+', 'substract': '-', 'multiply': '*', 'devide': '/'}

# def calculator(n1, n2, action):
#     return eval(f'{n1}{signs[action]}{n2}')

# print(calculator(2, 5, 'multiply'))
# score_1 = ['A','E','I','O','U','L','N','S','R','T']
# score_2 = ['D', 'G']
# score_3 = ['B','C','M''P']
# score_4 = ['F'"H"'V''W''Y']
# score_5 = ['K']
# score_8 = ['J', 'X']
# score_10 = ['Q', 'Z']


import re
def scrable(text):
    return bool(re.search("[а-яА-Я]", text))
letters_en = {
    1 : 'AEIOULNSTR', 
    2:'DG', 
    3: 'BCMP', 
    4: 'FHVWY', 
    5: 'K', 
    8: 'JX', 
    10: 'QZ'}
letters_ru = {
        1: 'АВЕИНОРСТ',
        2: 'ДКЛМПУ',
        3: 'БГЁЬЯ',
        4: 'ЙЫ',
        5: 'ЖЗХЦЧ',
        8: 'ШЭЮ',
        10:  'ФЩЪ'}
text = input().upper()

if scrable(text):
    print(sum([k for i in text for k, v in letters_ru.items() if i in v]))
else:
    print(sum([k for i in text for k, v in letters_en.items() if i in v]))








    


    