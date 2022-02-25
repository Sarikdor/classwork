# loops 

# two type of loops
# while 
# for

# for i in range(1, 11):
#     print(f'9 x {i} = {9 * i}')

# range(stop) -> [0; stop)
# range(start, stop) -> [start; stop)
# range(start, stop, step)
# def print_multi_table(num, from_num,up_to):
#     for i in range(from_num, up_to + 1):
#         print(f'{num} x {i} = {num * i}')

# print_multi_table(44, 7, 13)
# def print_exp_table(num, from_num,up_to):
#     for i in range(from_num, up_to + 1):
#         print(f'{num} ** {i} = {num ** i}')

# print_exp_table(2, 1, 6)
#! 
for letter in 'Sardor Khalillaev':
    if letter == ' ':
        print(letter)
#     else:
#         print(letter, end = '*' )
# print('sardor'. upper())
# print('SARDOR'. lower())
# print('S'. isupper())
# print('Sardor'. islower())
# new_str = ''
# for letter in 'Sardor Khalillaev':
#     new_str = new_str + letter.swapcase()
# print(new_str)