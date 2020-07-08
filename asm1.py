def first_digit(haha):
    number = haha
    while number >= 10:
        number = number // 10
    return number


i = 2
listnum = [1, 1]

while i <= 250:
    a = listnum[i - 2] + listnum[i - 1]
    listnum.append(a)
    i += 1
print(listnum)

first_numbers = {}
num = 0
while num < 250:
    cur_first = first_digit(listnum[num])
    if cur_first not in first_numbers:
        first_numbers[cur_first] = 1
    else:
        first_numbers[cur_first] += 1
    num += 1
first_numbers_percent = {}
for key,num in first_numbers.items():
    first_numbers_percent[key]= num/100

print(first_numbers)
print(first_numbers_percent)