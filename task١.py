

'''


def checkafford():
    badget = int(input('Enter the frist number :'))
    coast = int(input('Enter the second number :'))
    if badget>coast :
        reminig = badget -coast
        print(f'affordable : {reminig}')
    else:
        needed = coast - badget
        print(f'affordable : {needed}')
checkafford()        
'''
'''


def sentence():
    New_sentence = input('Enter the sentence :')
    return New_sentence.capitalize()
print(sentence())

'''


'''


def sum():
    frist_num = float(input('Enter the frist number :'))
    second_num = float(input('Enter the second number :'))
    sum = frist_num + second_num
    if sum > 100:
        print(f'{sum} : gretar than 100')
    else:
        print(f'{sum} : less than 100')

sum()
'''

'''


def remove_from_list():
    My_list = ['apple','banana','cherry','data']
    print(My_list)
    item_needed_to_remove = input('Enter item needed to remove :')
    if item_needed_to_remove in My_list:
        My_list.remove(item_needed_to_remove)
    else:
        print('item needed remove not found! ')

    print(My_list)
remove_from_list()    
'''


'''


def calculate_factorial():
    N = int(input('Enter a postive number :'))
    if N <0:
        print('please enter postive number !')
        return
    factorial1 = 1
    for n in range(1,N+1):
        factorial1*= n
    print(f'the factorial  {N} is {factorial1}')

calculate_factorial()


'''





























