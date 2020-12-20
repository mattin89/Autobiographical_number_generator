'''
By Mario De Lorenzo, md3466@drexel.edu

This script will generate any autobiographic number with N digits. The is_autobiographical() function will check if
numbers are indeed autobiographic numbers and, if so, it will store them inside a list. The main for loop will check
for sum of digits and if the number of 1s is 0, 1 or 2. After inserting the N digits, the script will tell you how long
it should take. You can decide which for loop condition to keep based on your purpose.
'''
import collections
from tqdm import tqdm

user = input("N digits: ")
b_list = []

def is_autobiographical(num):
    lst = list(map(int, list(num)))

    counts = collections.Counter(lst)

    return all(lst[i] == counts.get(i, 0) for i in range(len(lst)))

def check_ones(num): #The numbers of 1s can only be 0,1, or 2
    check = str(num)
    if num > 10:
        if int(check[1]) >= 3:
            return True
        else:
            return False
    else:
        return False

#for i in tqdm(range(10**(int(user)-1), 10**(int(user)))):  #Only N digits numbers
for i in tqdm(range(10**(int(user)))):   #All numbers up to N digits

    sum_of_digits = sum(int(digit) for digit in str(i))
    if sum_of_digits == len(str(i)): #Only checks the numbers that the sum of each digits is equal to the length
        if is_autobiographical(str(i)):
            b_list.append(i)

    if check_ones(i) and i > 10:
        temp = str(i)
        temp1 = int(temp[0])
        i = (temp1+1) * (10 ** (len(temp)-1))

print()
print(b_list)
