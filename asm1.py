import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def first_digit(haha):
    number = haha
    while number >= 10:
        number = number // 10
    return number
def last_digit(hah):
    return hah %10
i = 2
listnum = [1, 1]

while i <= 250:
    a = listnum[i - 2] + listnum[i - 1]
    listnum.append(a)
    i += 1
print(listnum)
## first number list
first_numbers = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
num = 0
while num < 250:
    cur_first = first_digit(listnum[num])
    first_numbers[cur_first] += 1
    num += 1
first_numbers_percent = {}
for key, num in first_numbers.items():
    first_numbers_percent[key] = num / 2.5

print(first_numbers)
print(first_numbers_percent)
## First plot
x = []
y = []
x = list(first_numbers_percent.keys())
y = list(first_numbers_percent.values())
plt.title("Fibonacci total rate of first digit")
axes2=plt.axes()
axes2.set_xlim([0,10])
axes2.set_xticks([1,2,3,4,5,6,7,8,9])
axes2.set_ylim([0,100])
plt.axhline(y=10, color="hotpink", linestyle="--")
plt.xlabel("First-digits")
plt.ylabel("Percentage")
plt.bar(x,y, color="coral", edgecolor="black")
plt.show()
##
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxx")
## last digit count
q=0
last_numbers = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
while q <250:
    cur_last= last_digit(listnum[q])
    last_numbers[cur_last]+=1
    q +=1
last_numbers_percent={}
for key, value in last_numbers.items():
    last_numbers_percent[key]= value/2.5
print(last_numbers)
print(last_numbers_percent)
## Last plot
x_last=[]
y_last=[]
x_last=list(last_numbers_percent.keys())
y_last=list(last_numbers_percent.values())
plt.xlabel("Last-digit")
plt.ylabel("Percentage")
plt.title("Fibonacci total rate of last digit")
plt.axhline(y=10, color="hotpink", linestyle="--")

axes1=plt.axes()
axes1.set_xlim([-1,10])
axes1.set_xticks([0,1,2,3,4,5,6,7,8,9])
axes1.set_ylim([0,100])
for x,y in zip(x_last,y_last):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
plt.bar(x_last,y_last, color ="pink")
plt.show()
